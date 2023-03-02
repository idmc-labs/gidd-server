import strawberry
from typing import List, Optional
from django.db.models import Max, Min
from django.utils import translation
from modeltranslation.utils import build_localized_fieldname
from apps.country.models import Country
from asgiref.sync import sync_to_async
from apps.good_practice.gh_filters import GoodPracticeFilter
from strawberry_django.filters import apply as filter_apply
from strawberry_django.pagination import (
    apply as pagination_apply,
    OffsetPaginationInput,
)
from strawberry_django.ordering import apply as ordering_apply
from strawberry.types import Info

from .models import GoodPractice, Faq, Tag
from .types import (
    FaqType,
    FaqListType,
    GoodPracticeType,
    PaginationBaseType,
    GoodPracticeOrder,
    GoodPracticeFilterChoiceType,
    GoodPracticeFilterCountryChoiceType,
    DriversOfDisplacementType,
    FocusAreaType,
    TagType,
)
from config.enums import GenericEnumValue, generate_enum_name_and_label


def faq_obj(pk) -> FaqType:
    return sync_to_async(Faq.objects.get, thread_sensitive=True)(
        pk=pk, is_published=True
    )


@sync_to_async
def faq_qs() -> List[FaqListType]:
    qs = Faq.objects.filter(is_published=True)
    return [
        FaqListType(
            id=faq.id,
            question=faq.question,
            answer=faq.answer,
        )
        for faq in qs
    ]


def good_practice_obj(pk) -> GoodPracticeType:
    return sync_to_async(GoodPractice.objects.get, thread_sensitive=True)(
        pk=pk, is_published=True
    )


@sync_to_async
def good_practice_qs(model) -> List[GoodPracticeType]:
    return model.objects.filter(is_published=True)


@sync_to_async
def get_good_practice_filter_options() -> GoodPracticeFilterChoiceType:
    active_language = translation.get_language()
    good_practice_qs = GoodPractice.objects.filter(is_published=True)
    types = list(
        good_practice_qs.filter(type__isnull=False)
        .distinct()
        .values_list("type", flat=True)
    )
    stages = list(
        good_practice_qs.filter(stage__isnull=False)
        .distinct()
        .values_list("stage", flat=True)
    )
    regions = list(
        good_practice_qs.filter(countries__good_practice_region__isnull=False)
        .distinct()
        .values_list("countries__good_practice_region", flat=True)
    )
    countries_dict = (
        good_practice_qs.filter(countries__isnull=False)
        .distinct()
        .values("countries")
        .order_by()
        .values("countries__id", "countries__name")
    )
    return GoodPracticeFilterChoiceType(
        type=[
            GenericEnumValue(
                name=GoodPractice.Type(type).name, label=GoodPractice.Type(type).label
            )
            for type in types
        ],
        drivers_of_displacement=[
            DriversOfDisplacementType(
                id=_id,
                name=name,
            )
            for _id, name in good_practice_qs.filter(
                drivers_of_displacement__isnull=False
            )
            .distinct("drivers_of_displacement__name")
            .order_by()
            .values_list(
                "drivers_of_displacement__id",
                f"drivers_of_displacement__{build_localized_fieldname('name', active_language)}",
            )
        ],
        stage=[
            GenericEnumValue(
                name=GoodPractice.StageType(type).name,
                label=GoodPractice.StageType(type).label,
            )
            for type in stages
        ],
        focus_area=[
            FocusAreaType(
                id=_id,
                name=name,
            )
            for _id, name in good_practice_qs.filter(focus_area__isnull=False)
            .distinct("focus_area__name")
            .order_by()
            .values_list(
                "focus_area__id",
                f"focus_area__{build_localized_fieldname('name', active_language)}",
            )
        ],
        regions=[
            GenericEnumValue(
                name=Country.GoodPracticeRegion(type).name,
                label=Country.GoodPracticeRegion(type).label,
            )
            for type in regions
        ],
        countries=[
            GoodPracticeFilterCountryChoiceType(
                id=country["countries__id"], name=country["countries__name"]
            )
            for country in countries_dict
        ],
        start_year=good_practice_qs.aggregate(Min("start_year"))["start_year__min"],
        end_year=good_practice_qs.aggregate(Max("end_year"))["end_year__max"],
        tags=[
            TagType(
                id=id,
                name=name,
            )
            for id, name in Tag.objects.values_list(
                "id",
                f"{build_localized_fieldname('name', active_language)}",
            )
        ],
    )


@sync_to_async
def get_graphql_objects(qs) -> List[GoodPracticeType]:
    return [
        GoodPracticeType(
            is_translated=good_practice_data.pop("title_fr") not in [None, ""],
            **good_practice_data,
        )
        for good_practice_data in qs.values(
            "id",
            "description",
            "end_year",
            "implementing_entity",
            "is_published",
            "media_and_resource_links",
            "page_viewed_count",
            "published_date",
            "stage",
            "start_year",
            "title",
            "title_fr",
            "type",
        )
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
        return [
            FaqType(id=faq.id, question=faq.question, answer=faq.answer) for faq in qs
        ]

    @strawberry.field
    async def good_practices(
        self,
        pagination: OffsetPaginationInput,
        ordering: GoodPracticeOrder,
        filters: Optional[GoodPracticeFilter] = None,
    ) -> PaginationBaseType:
        qs = await good_practice_qs(GoodPractice)

        if filters:
            qs = filter_apply(filters, qs)

        ordered_qyeryset = ordering_apply(ordering, qs)

        paginated_queryset = pagination_apply(pagination, ordered_qyeryset)

        results = await get_graphql_objects(paginated_queryset)

        total_count = await get_qs_count(ordered_qyeryset)

        return PaginationBaseType(results=results, total_count=total_count)

    @strawberry.field
    async def good_practice_filter_choices(self) -> GoodPracticeFilterChoiceType:
        options = await get_good_practice_filter_options()
        return options

    tags: List[TagType] = strawberry.django.field(pagination=True)

    drivers_of_displacements: List[DriversOfDisplacementType] = strawberry.django.field(
        pagination=True
    )

    focus_areas: List[FocusAreaType] = strawberry.django.field(pagination=True)

    @strawberry.field
    def good_practice_type_enums(self) -> List[GenericEnumValue[GoodPractice.Type]]:
        return generate_enum_name_and_label(GoodPractice.Type)

    @strawberry.field
    def good_practice_stage_type_enums(
        self,
    ) -> List[GenericEnumValue[GoodPractice.StageType]]:
        return generate_enum_name_and_label(GoodPractice.StageType)
