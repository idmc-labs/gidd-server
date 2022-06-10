# types.py
import strawberry
from strawberry import auto
from .models import StaticPage
from .enums import StaticPageTypeEnum
from .gh_filters import StaticPageFilter


@strawberry.django.type(StaticPage)
class StaticPageType:
    id: auto
    type: StaticPageTypeEnum
    description: auto


@strawberry.django.type(StaticPage, pagination=True, filters=StaticPageFilter)
class StaticPageListType(StaticPageType):
    pass
