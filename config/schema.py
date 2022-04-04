# schema.py
import strawberry
from apps.country.schema import Query as CountryQuery
from apps.country.mutations import Mutation as CountryMutation


@strawberry.type
class Query(CountryQuery):
    pass


@strawberry.type
class Mutation(CountryMutation):
    pass


schema = strawberry.Schema(query=Query, mutation=Mutation)
