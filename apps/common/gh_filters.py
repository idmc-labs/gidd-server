import strawberry
from typing import List
from .enums import StaticPageTypeEnum
from .models import StaticPage


@strawberry.django.filters.filter(StaticPage)
class StaticPageFilter:
    static_page_types: List[StaticPageTypeEnum] | None

    def filter_static_page_types(self, queryset):
        if not self.static_page_types:
            return queryset
        return queryset.filter(type__in=self.static_page_types)
