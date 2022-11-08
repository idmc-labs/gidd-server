# schema.py
import strawberry
import sentry_sdk

from django.conf import settings
from strawberry.types import ExecutionResult

from apps.country.schema import Query as CountryQuery
from apps.good_practice.schema import Query as GoodPracticeQuery
from apps.good_practice.mutations import Mutation as GoodPracticeMutation
from apps.common.schema import Query as CommonQuery


@strawberry.type
class Query(
    CountryQuery,
    GoodPracticeQuery,
    CommonQuery,
):
    pass


@strawberry.type
class Mutation(
    GoodPracticeMutation,
):
    pass


class Schema(strawberry.Schema):
    def _scope_with_sentry(self, execute_func, *args, **kwargs) -> ExecutionResult:
        if not settings.SENTRY_ENABLED:
            return execute_func(*args, **kwargs)
        operation_name = kwargs.get("operation_name")
        with sentry_sdk.configure_scope() as scope:
            scope.set_tag("kind", operation_name)
            scope.transaction.name = operation_name
            return execute_func(*args, **kwargs)

    def execute_sync(self, *args, **kwargs) -> ExecutionResult:
        return self._scope_with_sentry(super().execute_sync, *args, **kwargs)

    def execute(self, *args, **kwargs) -> ExecutionResult:
        return self._scope_with_sentry(super().execute, *args, **kwargs)


schema = Schema(query=Query, mutation=Mutation)
