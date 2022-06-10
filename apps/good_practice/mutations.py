from strawberry_django_plus import gql
from apps.good_practice.models import GoodPractice


@gql.django.type(GoodPractice)
class GoodPracticeType(gql.Node):
    id: gql.auto
    page_viewed_count: gql.auto


@gql.type
class Mutation:
    @gql.django.input_mutation
    def increment_page_viewed_count(self, info, id: gql.ID) -> GoodPracticeType:
        obj = GoodPractice.objects.get(id=id)
        obj.page_viewed_count = obj.page_viewed_count + 1
        obj.save()
        return obj
