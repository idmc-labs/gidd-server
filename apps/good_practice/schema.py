import strawberry
from typing import List, Optional
from django.db.models import Max, Min
from .types import (
    FaqType,
    FaqListType,
    GoodPracticeType,
    PaginationBaseType,
    GoodPracticeOrder,
    GoodPracticeFilterChoiceType,
    GoodPracticeFilterCountryChoiceType,
    EnumChoiceType,
)
from .models import GoodPractice, Faq
from apps.country.models import Country
from asgiref.sync import sync_to_async
from apps.good_practice.gh_filters import GoodPracticeFilter
from strawberry_django.filters import apply as filter_apply
from strawberry_django.pagination import apply as pagination_apply, OffsetPaginationInput
from strawberry_django.ordering import apply as ordering_apply
from django.forms.models import model_to_dict
from strawberry.types import Info


def faq_obj(pk) -> FaqType:
    return sync_to_async(
        Faq.objects.get, thread_sensitive=True
    )(pk=pk, is_published=True)


def good_practice_obj(pk) -> GoodPracticeType:
    return sync_to_async(
        GoodPractice.objects.get, thread_sensitive=True
    )(pk=pk, is_published=True)


@sync_to_async
def get_qs(model) -> List[GoodPracticeType]:
    return model.objects.filter(is_published=True)


@sync_to_async
def get_good_practice_filter_options() -> GoodPracticeFilterChoiceType:
    good_practice_qs = GoodPractice.objects.filter(is_published=True)
    types = list(
        good_practice_qs.filter(type__isnull=False).distinct().values_list('type', flat=True)
    )
    drivers_of_displacement = list(
        good_practice_qs.filter(
            drivers_of_displacement__isnull=False
        ).distinct().values_list('drivers_of_displacement', flat=True)
    )
    stages = list(
        good_practice_qs.filter(stage__isnull=False).distinct().values_list('stage', flat=True)
    )
    focus_areas = list(
        good_practice_qs.filter(focus_area__isnull=False).distinct().values_list('focus_area', flat=True)
    )
    regions = list(
        good_practice_qs.filter(countries__wb_region__isnull=False).distinct().values_list('countries__wb_region', flat=True)
    )
    countries_dict = good_practice_qs.filter(
        countries__isnull=False
    ).distinct().values('countries').order_by().values('countries__id', 'countries__name')
    return GoodPracticeFilterChoiceType(
        type=[
            EnumChoiceType(
                name=GoodPractice.Type(type).name,
                label=GoodPractice.Type(type).label
            ) for type in types
        ],
        drivers_of_displacement=[
            EnumChoiceType(
                name=GoodPractice.DriversOfDisplacementType(type).name,
                label=GoodPractice.DriversOfDisplacementType(type).label
            ) for type in drivers_of_displacement
        ],
        stage=[
            EnumChoiceType(
                name=GoodPractice.StageType(type).name,
                label=GoodPractice.StageType(type).label
            ) for type in stages
        ],
        focus_area=[
            EnumChoiceType(
                name=GoodPractice.FocusArea(type).name,
                label=GoodPractice.FocusArea(type).label,
            ) for type in focus_areas
        ],
        regions=[
            EnumChoiceType(
                name=Country.Region(type).name,
                label=Country.Region(type).label
            ) for type in regions
        ],
        countries=[
            GoodPracticeFilterCountryChoiceType(
                id=country['countries__id'],
                name=country['countries__name']
            ) for country in countries_dict
        ],
        start_year=good_practice_qs.aggregate(Min('start_year'))['start_year__min'],
        end_year=good_practice_qs.aggregate(Max('end_year'))['end_year__max'],
    )


def format_types(info, obj):
    result = model_to_dict(obj)
    result.pop('countries')
    result.pop('image')
    return result


@sync_to_async
def get_graphql_objects(info, qs) -> List[GoodPracticeType]:
    return [
        GoodPracticeType(
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

    @strawberry.field
    async def good_practice_filter_choices(self) -> GoodPracticeFilterChoiceType:
        options = await get_good_practice_filter_options()
        return options
