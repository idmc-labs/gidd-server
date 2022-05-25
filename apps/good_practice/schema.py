import strawberry
from typing import List, Optional
from .types import (
    FaqType,
    FaqListType,
    GoodPracticeMinType,
    GoodPracticeType,
    PaginationBaseType,
    GoodPracticeOrder,
)
from .models import GoodPractice, Faq
from asgiref.sync import sync_to_async
from apps.good_practice.gh_filters import GoodPracticeFilter
from strawberry_django.filters import apply as filter_apply
from strawberry_django.pagination import apply as pagination_apply, OffsetPaginationInput
from strawberry_django.ordering import apply as ordering_apply
from django.forms.models import model_to_dict
from django.db.models import FileField
from strawberry.types import Info
from utils import FileFieldType


def faq_obj(pk) -> FaqType:
    return sync_to_async(
        Faq.objects.get, thread_sensitive=True
    )(pk=pk, is_published=True)


def good_practice_obj(pk) -> GoodPracticeMinType:
    return sync_to_async(
        GoodPractice.objects.get, thread_sensitive=True
    )(pk=pk, is_published=True)


@sync_to_async
def get_qs(model) -> List[GoodPracticeMinType]:
    return model.objects.all()


def format_types(info, obj):
    result = model_to_dict(obj)
    result.pop('country')
    for field in obj._meta.fields:
        if isinstance(field, FileField):
            if obj.image:
                result['image'] = FileFieldType(
                    name=obj.image.name,
                    url=info.context['request'].build_absolute_uri(obj.image.url)
                )
            else:
                result['image'] = None
    return result


@sync_to_async
def get_graphql_objects(info, qs) -> List[GoodPracticeMinType]:
    return [
        GoodPracticeMinType(
            **format_types(info, good_practice)
        ) for good_practice in qs
    ]


@sync_to_async
def get_qs_count(qs) -> int:
    return qs.count()


@strawberry.type
class Query:
    @strawberry.field
    def faq(self, pk: strawberry.ID) -> FaqType:
        return faq_obj(pk)

    @strawberry.field
    def good_practice(self, pk: strawberry.ID) -> GoodPracticeType:
        return good_practice_obj(pk)

    faqs: List[FaqListType] = strawberry.django.field()

    @strawberry.field
    async def good_practices(
        self,
        info: Info,
        filters: Optional[GoodPracticeFilter],
        pagination: OffsetPaginationInput,
        ordering: GoodPracticeOrder,
    ) -> PaginationBaseType:
        qs = await get_qs(GoodPractice)

        if filters:
            qs = filter_apply(filters, qs)

        ordered_qyeryset = ordering_apply(ordering, qs)

        paginated_queryset = pagination_apply(pagination, ordered_qyeryset)

        results = await get_graphql_objects(info, paginated_queryset)

        total_count = await get_qs_count(paginated_queryset)

        return PaginationBaseType(
            results=results,
            total_count=total_count
        )
