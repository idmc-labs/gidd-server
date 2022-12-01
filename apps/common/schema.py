import strawberry
from typing import List

from .types import (
    StaticPageType,
    StaticPageListType,
)


@strawberry.type
class Query:
    static_pages: List[StaticPageListType] = strawberry.django.field()
    static_page: StaticPageType = strawberry.django.field()
