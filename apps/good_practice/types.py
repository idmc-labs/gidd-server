# types.py
import strawberry
from strawberry import auto
from typing import List

from .models import (
    Faq, GoodPractice, Gallery
)
from .gh_filters import GoodPracticeFilter, FaqFilter

from .enums import (
    TypeEnum,
    DriversOfDisplacementTypeEnum,
    StageTypeEnum,
    FocusAreaEnum,
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


@strawberry.django.type(GoodPractice)
class GoodPracticeType:
    id: auto
    title: auto
    description: auto
    type: TypeEnum
    drivers_of_dispalcement: DriversOfDisplacementTypeEnum
    stage: StageTypeEnum
    good_practice_form_url: auto
    focus_area: FocusAreaEnum
    is_published: auto
    good_practice_form_url: auto
    image: Optional[FileFieldType]
    published_date: auto
    media_and_resource_links: auto
    start_year: auto
    end_year: auto
    page_viewed_count: auto

    @strawberry.field
    async def gallery(self, info: Info) -> List[GalleryType]:
        return await info.context["gallery_loader"].load(self.id)

    @strawberry.field
    async def countries(self, info: Info) -> List[CountryType]:
        return await info.context["good_practice_country_loader"].load(self.id)


@strawberry_django.ordering.order(GoodPractice)
class GoodPracticeOrder:
    id: auto
    title: auto
    description: auto
    good_practice_form_url: auto
    focus_area: auto
    is_published: auto
    page_viewed_count: auto


@strawberry.type
class GoodPracticeFilterChoiceType:
    type: Optional[List[str]]
    drivers_of_dispalcement: Optional[List[str]]
    stage: Optional[List[str]]
    focus_area: Optional[List[str]]
    regions: Optional[List[str]]


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
