import strawberry
from typing import List
from .types import (
    FaqType,
    FaqListType,
    GoodPracticeType,
    GoodPracticeListType,
)


@strawberry.type
class Query:
    faqs: List[FaqListType] = strawberry.django.field()
    good_practicies: List[GoodPracticeListType] = strawberry.django.field()
    faq: FaqType = strawberry.django.field()
    good_practice: GoodPracticeType = strawberry.django.field()
