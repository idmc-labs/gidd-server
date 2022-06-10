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
    DriversOfDisplacementType,
    FocusAreaType,
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


@sync_to_async
def faq_qs() -> List[FaqListType]:
    qs = Faq.objects.filter(is_published=True)
    return [
        FaqListType(
            id=faq.id,
            question=faq.question,
            answer=faq.answer,
        ) for faq in qs
    ]


def good_practice_obj(pk) -> GoodPracticeType:
    return sync_to_async(
        GoodPractice.objects.get, thread_sensitive=True
    )(pk=pk, is_published=True)


@sync_to_async
def good_practice_qs(model) -> List[GoodPracticeType]:
    return model.objects.filter(is_published=True)


@sync_to_async
def get_good_practice_filter_options() -> GoodPracticeFilterChoiceType:
    good_practice_qs = GoodPractice.objects.filter(is_published=True)
    types = list(
        good_practice_qs.filter(type__isnull=False).distinct().values_list('type', flat=True)
    )
    stages = list(
        good_practice_qs.filter(stage__isnull=False).distinct().values_list('stage', flat=True)
    )
    regions = list(
        good_practice_qs.filter(
            countries__good_practice_region__isnull=False
        ).distinct().values_list('countries__good_practice_region', flat=True)
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
            DriversOfDisplacementType(
                name=driver_of_displacement['drivers_of_displacement__name'],
                id=driver_of_displacement['drivers_of_displacement__id'],
            ) for driver_of_displacement in good_practice_qs.filter(drivers_of_displacement__isnull=False).distinct(
                'drivers_of_displacement__name'
            ).order_by().values('drivers_of_displacement__id', 'drivers_of_displacement__name')
        ],
        stage=[
            EnumChoiceType(
                name=GoodPractice.StageType(type).name,
                label=GoodPractice.StageType(type).label
            ) for type in stages
        ],
        focus_area=[
            FocusAreaType(
                name=focus_area['focus_area__name'],
                id=focus_area['focus_area__id'],
            ) for focus_area in good_practice_qs.filter(focus_area__isnull=False).distinct(
                'focus_area__name'
            ).order_by().values('focus_area__id', 'focus_area__name')
        ],
        regions=[
            EnumChoiceType(
                name=Country.GoodPracticeRegion(type).name,
                label=Country.GoodPracticeRegion(type).label
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
    result.pop('tags')
    result.pop('drivers_of_displacement')
    result.pop('focus_area')
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

    @strawberry.field
    async def faqs(self, info: Info) -> List[FaqListType]:
        qs = await faq_qs()
        return [FaqType(id=faq.id, question=faq.question, answer=faq.answer) for faq in qs]

    @strawberry.field
    async def good_practices(
        self,
        info: Info,
        filters: Optional[GoodPracticeFilter],
        pagination: OffsetPaginationInput,
        ordering: GoodPracticeOrder,
    ) -> PaginationBaseType:
        qs = await good_practice_qs(GoodPractice)

        if filters:
            qs = filter_apply(filters, qs)

        ordered_qyeryset = ordering_apply(ordering, qs)

        paginated_queryset = pagination_apply(pagination, ordered_qyeryset)

        results = await get_graphql_objects(info, paginated_queryset)

        total_count = await get_qs_count(ordered_qyeryset)

        return PaginationBaseType(
            results=results,
            total_count=total_count
        )

    @strawberry.field
    async def good_practice_filter_choices(self) -> GoodPracticeFilterChoiceType:
        options = await get_good_practice_filter_options()
        return options
