# types.py
import strawberry
from strawberry import auto
from typing import List

from .models import (
    Faq,
    GoodPractice,
    Gallery,
    Tag,
    DriversOfDisplacement,
    FocusArea,
    SuccessFactor,
)
from .gh_filters import GoodPracticeFilter, FaqFilter

from .enums import (
    TypeEnum,
    StageTypeEnum,
)
from apps.country.types import GiddCountryType
from apps.country.models import Country
import strawberry_django
from typing import Optional
from utils import FileFieldType, build_url, get_enum_label
from strawberry.types import Info
from config.enums import GenericEnumValue


@strawberry.django.type(Faq, pagination=True)
class FaqType:
    id: auto
    question: auto
    answer: auto


@strawberry.django.type(Faq, pagination=True, filters=FaqFilter)
class FaqListType(FaqType):
    pass


@strawberry.django.type(Gallery)
class GalleryType:
    id: auto
    youtube_video_url: auto
    caption: auto

    @strawberry.field
    async def image(self, info: Info) -> Optional[FileFieldType]:
        return build_url(self.image, info.context["request"])


@strawberry.django.type(Tag)
class TagType:
    id: auto
    name: auto


@strawberry.django.type(DriversOfDisplacement)
class DriversOfDisplacementType:
    id: auto
    name: auto


@strawberry.django.type(FocusArea)
class FocusAreaType:
    id: auto
    name: auto


@strawberry.django.type(SuccessFactor)
class SuccessFactorType:
    id: auto
    name: auto


@strawberry.django.type(GoodPractice)
class GoodPracticeType:
    id: auto
    title: auto
    description: auto
    type: str
    stage: str
    is_published: auto
    published_date: auto
    media_and_resource_links: auto
    start_year: auto
    end_year: auto
    page_viewed_count: auto
    implementing_entity: auto
    contact_name: auto
    contact_email: auto
    what_makes_this_promising_practice: auto
    description_of_key_lessons_learned: auto
    under_review: auto

    is_translated: bool

    @strawberry.field
    async def image(self, info: Info) -> Optional[FileFieldType]:
        result = await info.context["good_practice_image_loader"].load(self.id)
        return build_url(result, info.context["request"])

    @strawberry.field
    async def gallery(self, info: Info) -> List[GalleryType]:
        return await info.context["gallery_loader"].load(self.id)

    @strawberry.field
    async def countries(self, info: Info) -> List[GiddCountryType]:
        return await info.context["good_practice_country_loader"].load(self.id)

    @strawberry.field
    async def tags(self, info: Info) -> Optional[List[TagType]]:
        return await info.context["good_practice_tags_loader"].load(self.id)

    @strawberry.field
    async def driver_of_displacement(
        self, info: Info
    ) -> Optional[List[DriversOfDisplacementType]]:
        return await info.context["good_practice_driver_of_displacement_loader"].load(
            self.id
        )

    @strawberry.field
    async def focus_area(self, info: Info) -> Optional[List[FocusAreaType]]:
        return await info.context["good_practice_focus_area_loader"].load(self.id)

    @strawberry.field
    async def type_label(self, info: Info) -> Optional[str]:
        return get_enum_label(TypeEnum, self.type)

    @strawberry.field
    async def stage_label(self, info: Info) -> str:
        return get_enum_label(StageTypeEnum, self.stage)

    @strawberry.field
    async def success_factor(
        self, info: Info
    ) -> List[SuccessFactorType]:
        return await info.context["good_practice_success_factor_loader"].load(
            self.id
        )


@strawberry_django.ordering.order(GoodPractice)
class GoodPracticeOrder:
    id: auto
    title: auto
    description: auto
    focus_area: auto
    is_published: auto
    page_viewed_count: auto
    published_date: auto
    updated_at: auto


@strawberry.type
class GoodPracticeFilterCountryChoiceType:
    id: strawberry.ID
    name: str


@strawberry.type
class GoodPracticeFilterChoiceType:
    type: Optional[List[GenericEnumValue[GoodPractice.Type]]]
    drivers_of_displacement: Optional[List[DriversOfDisplacementType]]
    stage: Optional[List[GenericEnumValue[GoodPractice.StageType]]]
    focus_area: Optional[List[FocusAreaType]]
    regions: Optional[List[GenericEnumValue[Country.GoodPracticeRegion]]]
    countries: Optional[List[GoodPracticeFilterCountryChoiceType]]
    tags: Optional[List[TagType]]
    start_year: int
    end_year: int
    success_factor: List[SuccessFactorType]


@strawberry.django.type(
    GoodPractice, pagination=True, filters=GoodPracticeFilter, order=GoodPracticeOrder
)
class GoodPracticeListType(GoodPracticeType):
    pass


@strawberry.input
class OffsetPaginationInput:
    offset: int = 0
    limit: int = -1


@strawberry.type()
class PaginationBaseType:
    results: List[GoodPracticeType]
    total_count: int


@strawberry_django.input(GoodPractice, partial=True)
class PageViewedInputType:
    id: auto
