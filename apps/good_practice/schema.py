import strawberry
from typing import List
from .types import (
    FaqType,
    FaqListType,
    GoodPracticeType,
    GoodPracticeListType,
)
from .models import GoodPractice, Faq
from asgiref.sync import sync_to_async


def faq_obj(pk) -> FaqType:
    return sync_to_async(
        Faq.objects.get, thread_sensitive=True
    )(pk=pk, is_published=True)


def good_practice_obj(pk) -> GoodPracticeType:
    return sync_to_async(
        GoodPractice.objects.get, thread_sensitive=True
    )(pk=pk, is_published=True)


@strawberry.type
class Query:
    @strawberry.field
    def faq(self, pk: strawberry.ID) -> FaqType:
        return faq_obj(pk)

    @strawberry.field
    def good_practice(self, pk: strawberry.ID) -> GoodPracticeType:
        return good_practice_obj(pk)

    faqs: List[FaqListType] = strawberry.django.field()
    good_practicies: List[GoodPracticeListType] = strawberry.django.field()
