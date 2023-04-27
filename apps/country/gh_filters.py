import strawberry
from strawberry import auto
from django.db.models import Q
from .models import (
    Country,
    CountryAdditionalInfo,
)


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
