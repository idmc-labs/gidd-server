import strawberry
from strawberry import auto
from django.db.models import Q
from .models import (
    Country,
    CountryAdditionalInfo,
    FigureAnalysis,
)
from typing import List
from .enums import CrisisTypeEnum


@strawberry.django.filters.filter(Country, lookups=True)
class CountryFilter:
    id: auto
    iso3: auto
    name: auto
    idmc_names: auto
    search: str | None

    def filter_search(self, queryset):
        if not self.search:
            return queryset
        return queryset.filter(
            Q(name__icontains=self.search) |
            Q(idmc_names__icontains=self.search) |
            Q(iso3__icontains=self.search)
        )


@strawberry.django.filters.filter(CountryAdditionalInfo, lookups=True)
class CountryAdditionalInfoFilter:
    id: auto


@strawberry.django.filters.filter(FigureAnalysis)
class FigureAnalysisFilter:
    year: auto
    crisis_types: List[CrisisTypeEnum]
    countries: List[strawberry.ID]

    def filter_countries(self, queryset):
        if not self.countries:
            return queryset
        return queryset.filter(country__in=self.countries)

    def filter_crisis_types(self, queryset):
        if not self.crisis_types:
            return queryset
        return queryset.filter(crisis_type__in=self.crisis_types)
