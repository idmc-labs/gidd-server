# types.py
import strawberry
from strawberry import auto
from typing import List

from .models import (
    Faq, GoodPractice, Gallery, Tag, DriversOfDisplacement, FocusArea,
)
from .gh_filters import GoodPracticeFilter, FaqFilter

from .enums import (
    TypeEnum,
    StageTypeEnum,
)
from apps.country.types import CountryType
import strawberry_django
from typing import Optional
from utils import FileFieldType, build_url
from strawberry.types import Info


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
        return build_url(self.image, info.context['request'])


@strawberry.django.type(Tag)
class TagType:
    id: auto
    name: auto


@strawberry.django.type(DriversOfDisplacement)
class DriversOfDisplacementType:
    id: int
    name: auto


@strawberry.django.type(FocusArea)
class FocusAreaType:
    id: int
    name: auto


@strawberry.django.type(GoodPractice)
class GoodPracticeType:
    id: auto
    title: auto
    description: auto
    type: TypeEnum
    stage: StageTypeEnum
    is_published: auto
    published_date: auto
    media_and_resource_links: auto
    start_year: auto
    end_year: auto
    page_viewed_count: auto

    @strawberry.field
    async def image(self, info: Info) -> Optional[FileFieldType]:
        result = await info.context["good_practice_image_loader"].load(self.id)
        return build_url(result, info.context['request'])

    @strawberry.field
    async def gallery(self, info: Info) -> List[GalleryType]:
        return await info.context["gallery_loader"].load(self.id)

    @strawberry.field
    async def countries(self, info: Info) -> List[CountryType]:
        return await info.context["good_practice_country_loader"].load(self.id)

    @strawberry.field
    async def tags(self, info: Info) -> Optional[List[TagType]]:
        return await info.context["good_practice_tags_loader"].load(self.id)

    @strawberry.field
    async def driver_of_displacement(self, info: Info) -> Optional[List[DriversOfDisplacementType]]:
        return await info.context["good_practice_driver_of_displacement_loader"].load(self.id)

    @strawberry.field
    async def focus_area(self, info: Info) -> Optional[List[FocusAreaType]]:
        return await info.context["good_practice_focus_area_loader"].load(self.id)


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
    id: int
    name: str


@strawberry.type
class EnumChoiceType:
    name: str
    label: str


@strawberry.type
class GoodPracticeFilterChoiceType:
    type: Optional[List[EnumChoiceType]]
    drivers_of_displacement: Optional[List[DriversOfDisplacementType]]
    stage: Optional[List[EnumChoiceType]]
    focus_area: Optional[List[FocusAreaType]]
    regions: Optional[List[EnumChoiceType]]
    countries: Optional[List[GoodPracticeFilterCountryChoiceType]]
    start_year: int
    end_year: int


@strawberry.django.type(GoodPractice, pagination=True, filters=GoodPracticeFilter, order=GoodPracticeOrder)
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
