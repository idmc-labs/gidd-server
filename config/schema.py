# schema.py
import strawberry
from apps.country.schema import Query as CountryQuery
from apps.good_practice.schema import Query as GoodPracticeQuery
from apps.good_practice.mutations import Mutation as GoodPracticeMutation


@strawberry.type
class Query(CountryQuery, GoodPracticeQuery):
    pass


@strawberry.type
class Mutation(GoodPracticeMutation):
    pass


schema = strawberry.Schema(query=Query, mutation=Mutation)
