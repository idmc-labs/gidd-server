# types.py
import strawberry
from strawberry.django import auto
# import strawberry_django
from .models import (
    Faq, GoodPractice, MediaAndResourceLink
)
from .gh_filters import GoodPracticeFilter
# from typing import List
# from strawberry.types import Info
from .enums import (
    TypeEnum,
    DriversOfDisplacementTypeEnum,
    TriggerTypeEnum,
    DisplacementImpactTypeEnum,
    InterventionPhaseTypeEnum,
    StageTypeEnum,
    TimeframeTypeEnum,
)
from apps.country.types import CountryType


@strawberry.django.type(Faq, pagination=True)
class FaqType:
    id: auto
    question: auto
    answer: auto


@strawberry.django.type(Faq, pagination=True)
class FaqListType(FaqType):
    pass


@strawberry.django.type(MediaAndResourceLink, pagination=True)
class MediaAndResourceLinkType:
    id: auto
    link: auto


@strawberry.django.type(GoodPractice)
class GoodPracticeType:
    id: auto
    title: auto
    description: auto
    country: CountryType
    type: TypeEnum
    drivers_of_dispalcement: DriversOfDisplacementTypeEnum
    trigger: TriggerTypeEnum
    dispalcement_impact: DisplacementImpactTypeEnum
    intervention_phase: InterventionPhaseTypeEnum
    stage: StageTypeEnum
    timeframe: TimeframeTypeEnum


@strawberry.django.type(GoodPractice, pagination=True, filters=GoodPracticeFilter)
class GoodPracticeListType(GoodPracticeType):
    pass
