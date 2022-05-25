# types.py
import strawberry
from strawberry.django import auto
from typing import List
from asgiref.sync import sync_to_async

from .models import (
    Faq, GoodPractice, MediaAndResourceLink
)
from .gh_filters import GoodPracticeFilter, FaqFilter
from .enums import (
    TypeEnum,
    DriversOfDisplacementTypeEnum,
    StageTypeEnum,
)
from apps.country.types import CountryType
import strawberry_django


@strawberry.django.type(Faq, pagination=True)
class FaqType:
    id: auto
    question: auto
    answer: auto


@strawberry.django.type(Faq, pagination=True, filters=FaqFilter)
class FaqListType(FaqType):
    pass


@strawberry.django.type(MediaAndResourceLink, pagination=True)
class MediaAndResourceLinkType:
    id: auto
    link: auto


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
    focus_area: auto
    is_published: auto
    image: auto


@strawberry.django.type(GoodPractice)
class GoodPracticeMinType:
    id: auto
    title: auto
    description: auto
    type: TypeEnum
    drivers_of_dispalcement: DriversOfDisplacementTypeEnum
    stage: StageTypeEnum
    good_practice_form_url: auto
    focus_area: auto
    is_published: auto
    image: auto


@strawberry_django.ordering.order(GoodPractice)
class GoodPracticeOrder:
    id: auto
    title: auto
    description: auto
    good_practice_form_url: auto
    focus_area: auto
    is_published: auto


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
