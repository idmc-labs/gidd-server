import asyncio
import contextlib
import contextvars
import inspect
from typing import Any, Dict, Optional, Union

from django.db import DEFAULT_DB_ALIAS, connections
from django.test.client import AsyncClient  # type:ignore
from django.test.client import Client
from django.test.utils import CaptureQueriesContext
from django.test import TestCase as BaseTestCase
from strawberry.test.client import Response


from strawberry_django_plus.test.client import TestClient

_client: contextvars.ContextVar["GraphQLTestClient"] = contextvars.ContextVar("_client_ctx")


class TestCase(BaseTestCase):
    TEST_LANGUAGES = ('en', 'fr',)

    def force_login(self, user):
        self.client.force_login(user)

    def logout(self):
        self.client.logout()

    def query_check(
        self,
        query: str,
        with_assert: bool = True,
        variables: dict | None = None,
        **kwargs,
    ) -> Dict:
        response = self.client.post(
            "/graphql/",
            data={
                "query": query,
                "variables": variables,
            },
            content_type="application/json",
            **kwargs,
        )
        if with_assert:
            self.assertEqual(response.status_code, 200)
        return response.json()

    def assertResponseNoErrors(self, resp, msg=None):
        """
        Assert that the call went through correctly. 200 means the syntax is ok,
        if there are no `errors`,
        the call was fine.
        :resp HttpResponse: Response
        """
        content = resp.json()
        self.assertEqual(resp.status_code, 200, msg or content)
        self.assertNotIn("errors", list(content.keys()), msg or content)

    def assertResponseHasErrors(self, resp, msg=None):
        """
        Assert that the call was failing. Take care: Even with errors,
        GraphQL returns status 200!
        :resp HttpResponse: Response
        """
        content = resp.json()
        self.assertIn("errors", list(content.keys()), msg or content)


class FakeTest(TestCase):
    """
    This test is for running migrations only
    docker-compose run --rm server ./manage.py test -v 2 --pattern="config/tests/test_fake.py"
    """
    def test_fake(self):
        pass


@contextlib.contextmanager
def assert_num_queries(n: int, *, using=DEFAULT_DB_ALIAS):
    with CaptureQueriesContext(connection=connections[DEFAULT_DB_ALIAS]) as ctx:
        yield

    executed = len(ctx)

    # FIXME: Why async is failing to track queries? Like, 0?
    if _client.get().is_async and executed == 0:
        return

    assert executed == n, "{} queries executed, {} expected\nCaptured queries were:\n{}".format(
        executed,
        n,
        "\n".join(f"{i}. {q['sql']}" for i, q in enumerate(ctx.captured_queries, start=1)),
    )


class GraphQLTestClient(TestClient):
    def __init__(
        self,
        path: str,
        client: Union[Client, AsyncClient],
    ):
        super().__init__(path, client=client)
        self._token: Optional[contextvars.Token] = None
        self.is_async = isinstance(client, AsyncClient)

    def __enter__(self):
        self._token = _client.set(self)
        return self

    def __exit__(self, *args, **kwargs):
        assert self._token
        _client.reset(self._token)

    def request(
        self,
        body: Dict[str, object],
        headers: Optional[Dict[str, object]] = None,
        files: Optional[Dict[str, object]] = None,
    ):
        kwargs: Dict[str, object] = {"data": body}
        if files:  # pragma:nocover
            kwargs["format"] = "multipart"
        else:
            kwargs["content_type"] = "application/json"

        return self.client.post(self.path, **kwargs)

    def query(
        self,
        query: str,
        variables: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, object]] = None,
        asserts_errors: Optional[bool] = True,
        files: Optional[Dict[str, object]] = None,
    ) -> Response:
        body = self._build_body(query, variables, files)

        resp = self.request(body, headers, files)
        if inspect.iscoroutine(resp):
            resp = asyncio.run(resp)

        data = self._decode(resp, type="multipart" if files else "json")

        response = Response(
            errors=data.get("errors"),
            data=data.get("data"),
            extensions=data.get("extensions"),
        )
        if asserts_errors:
            assert response.errors is None

        return response
