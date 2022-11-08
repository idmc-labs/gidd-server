from typing import Dict

from django.test import TestCase as BaseTestCase


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
