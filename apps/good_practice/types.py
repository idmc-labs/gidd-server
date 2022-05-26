# types.py
import strawberry
from strawberry import auto
from typing import List
from asgiref.sync import sync_to_async

from .models import (
    Faq, GoodPractice
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
from utils import FileFieldType


@strawberry.django.type(Faq, pagination=True)
class FaqType:
    id: auto
    question: auto
    answer: auto


@strawberry.django.type(Faq, pagination=True, filters=FaqFilter)
class FaqListType(FaqType):
    pass


@sync_to_async
def good_practice_count() -> int:
    return GoodPractice.objects.count()


@strawberry.django.type(GoodPractice)
class GoodPracticeType:
    id: auto
    title: auto
    description: auto
    country: CountryType
    type: TypeEnum
    drivers_of_dispalcement: DriversOfDisplacementTypeEnum
    stage: StageTypeEnum
    good_practice_form_url: auto
    focus_area: FocusAreaEnum
    is_published: auto
    good_practice_form_url: auto
    image: auto
    published_date: auto
    media_and_resource_links: auto
    start_year: auto
    end_year: auto
    page_viewed_count: auto


@strawberry.django.type(GoodPractice)
class GoodPracticeMinType:
    id: auto
    title: auto
    description: auto
    type: TypeEnum
    drivers_of_dispalcement: DriversOfDisplacementTypeEnum
    stage: StageTypeEnum
    good_practice_form_url: auto
    focus_area: FocusAreaEnum
    is_published: auto
    image: Optional[FileFieldType]
    published_date: auto
    media_and_resource_links: auto
    start_year: auto
    end_year: auto
    page_viewed_count: auto


@strawberry_django.ordering.order(GoodPractice)
class GoodPracticeOrder:
    id: auto
    title: auto
    description: auto
    good_practice_form_url: auto
    focus_area: auto
    is_published: auto
    page_viewed_count: auto


@strawberry.django.type(GoodPractice, pagination=True, filters=GoodPracticeFilter, order=GoodPracticeOrder)
class GoodPracticeListType(GoodPracticeMinType):
    pass


@strawberry.input
class OffsetPaginationInput:
    offset: int = 0
    limit: int = -1


@strawberry.type()
class PaginationBaseType:
    results: List[GoodPracticeMinType]
    total_count: int


@strawberry_django.input(GoodPractice, partial=True)
class PageViewedInputType:
    id: auto
