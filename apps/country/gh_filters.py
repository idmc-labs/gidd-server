import strawberry
from strawberry.django import auto
from .models import (
    Country,
    CountryAdditionalInfo,
    Conflict,
    Disaster,
)


@strawberry.django.filters.filter(Country, lookups=True)
class CountryFilter:
    id: auto
    iso3: auto


@strawberry.django.filters.filter(CountryAdditionalInfo, lookups=True)
class CountryAdditionalInfoFilter:
    id: auto


@strawberry.django.filters.filter(Conflict, lookups=True)
class ConflictFilter:
    id: auto


@strawberry.django.filters.filter(Disaster, lookups=True)
class DisasterFilter:
    id: auto
