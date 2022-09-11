import strawberry
from strawberry import auto
from django.db.models import Q
from .models import (
    Country,
    CountryAdditionalInfo,
    Conflict,
    Disaster,
)
from typing import List
from .enums import IdmcRegionEnum

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


@strawberry.django.filters.filter(Conflict, lookups=True)
class ConflictFilter:
    id: auto


@strawberry.django.filters.filter(Disaster, lookups=True)
class DisasterFilter:
    id: auto


@strawberry.django.filters.filter(Conflict, lookups=True)
class ConflictStatisticsFilter:
    countries: List[strawberry.ID] | None
    start_year: int | None
    end_year: int | None
    countries_iso3: List[str] | None

    def filter_years(self, queryset):
        if not self.years:
            return queryset
        return queryset.filter(year__in=self.years)

    def filter_countries(self, queryset):
        if not self.countries:
            return queryset
        return queryset.filter(country__in=self.countries)

    def filter_start_year(self, queryset):
        if not self.start_year:
            return queryset
        return queryset.filter(year__gte=self.start_year)

    def filter_end_year(self, queryset):
        if not self.end_year:
            return queryset
        return queryset.filter(year__lte=self.end_year)

    def filter_countries_iso3(self, queryset):
        if not self.countries_iso3:
            return queryset
        return queryset.filter(country__iso3__in=self.countries_iso3)

    @property
    def qs(self):
        from .types import conflict_statistics_qs
        qs = super().qs
        return conflict_statistics_qs(qs)


@strawberry.django.filters.filter(Disaster, lookups=True)
class DisasterStatisticsFilter:
    categories: List[str] | None
    countries: List[strawberry.ID] | None
    start_year: int | None
    end_year: int | None
    countries_iso3: List[str] | None
    regions: List[IdmcRegionEnum] | None

    def filter_categories(self, queryset):
        if not self.categories:
            return queryset
        return queryset.filter(hazard_type__in=self.categories)

    def filter_countries(self, queryset):
        if not self.countries:
            return queryset
        return queryset.filter(country__in=self.countries)

    def filter_start_year(self, queryset):
        if not self.start_year:
            return queryset
        return queryset.filter(year__gte=self.start_year)

    def filter_end_year(self, queryset):
        if not self.end_year:
            return queryset
        return queryset.filter(year__lte=self.end_year)

    def filter_countries_iso3(self, queryset):
        if not self.countries_iso3:
            return queryset
        return queryset.filter(country__iso3__in=self.countries_iso3)

    def filter_regions(self, queryset):
        if not self.regions:
            return queryset
        return queryset.filter(country__idmc_region__in=self.regions)

    @property
    def qs(self):
        from .types import disaster_statistics_qs
        qs = super().qs
        return disaster_statistics_qs(qs)
