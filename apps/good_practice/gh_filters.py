from django.db.models import Q
from strawberry import auto

from .models import (
    GoodPractice, Faq,
)
import strawberry
from .enums import (
    TypeEnum,
    StageTypeEnum,
)
from typing import List
from apps.country.enums import GoodPracticeRegionEnum


@strawberry.django.filters.filter(GoodPractice)
class GoodPracticeFilter:
    search: str | None
    types: List[TypeEnum] | None
    drivers_of_displacements: List[strawberry.ID] | None
    stages: List[StageTypeEnum] | None
    countries: List[strawberry.ID] | None
    regions: List[GoodPracticeRegionEnum] | None
    focus_area: List[strawberry.ID] | None
    start_year: int | None
    end_year: int | None
    recommended_good_practice: strawberry.ID

    def filter_search(self, queryset):
        if not self.search:
            return queryset
        return queryset.filter(
            Q(title__icontains=self.search) |
            Q(description__icontains=self.search)
        )

    def filter_types(self, queryset):
        if not self.types:
            return queryset
        return queryset.filter(type__in=self.types)

    def filter_drivers_of_displacements(self, queryset):
        if not self.drivers_of_displacements:
            return queryset
        return queryset.filter(drivers_of_displacement__in=self.drivers_of_displacements)

    def filter_trigger_types(self, queryset):
        if not self.trigger_types:
            return queryset
        return queryset.filter(trigger__in=self.trigger_types)

    def filter_stages(self, queryset):
        if not self.stages:
            return queryset
        return queryset.filter(stage__in=self.stages)

    def filter_countries(self, queryset):
        if not self.countries:
            return queryset
        return queryset.filter(countries__in=self.countries)

    def filter_regions(self, queryset):
        if not self.regions:
            return queryset
        return queryset.filter(countries__good_practice_region__in=self.regions).distinct()

    def filter_focus_area(self, queryset):
        if not self.focus_area:
            return queryset
        return queryset.filter(focus_area__in=self.focus_area)

    def filter_start_year(self, queryset):
        if not self.start_year:
            return queryset
        return queryset.filter(start_year__gte=self.start_year)

    def filter_end_year(self, queryset):
        if not self.end_year:
            return queryset
        return queryset.filter(
            (Q(end_year__lte=self.end_year) & Q(start_year__gte=self.start_year)) |
            Q(start_year__lte=self.end_year, end_year__isnull=True)
        ).distinct()

    def filter_recommended_good_practice(self, queryset):
        if not self.recommended_good_practice:
            return queryset
        good_practice_qs = GoodPractice.objects.filter(id=self.recommended_good_practice)
        return queryset.filter(
            Q(focus_area__in=good_practice_qs.values('focus_area')) |
            Q(type__in=good_practice_qs.values('type')) |
            Q(drivers_of_displacement__in=good_practice_qs.values('drivers_of_displacement')) |
            Q(stage__in=good_practice_qs.values('stage'))
        ).exclude(id=self.recommended_good_practice).distinct('id')

    @property
    def qs(self):
        return super().qs.filter(is_published=True).distinct()


@strawberry.django.filters.filter(Faq)
class FaqFilter:
    question: auto

    @property
    def qs(self):
        return super().qs.filter(is_published=True)
