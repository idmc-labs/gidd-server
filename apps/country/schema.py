import strawberry
from typing import List, Optional
from .types import (
    GiddCountryType,
    GiddCountryListType,
)
from asgiref.sync import sync_to_async
from .models import Country


@sync_to_async
def get_country_object(pk, iso3):
    if pk:
        return Country.objects.get(pk=pk)
    if iso3:
        return Country.objects.get(iso3=iso3)


@strawberry.type
class Query:
    country_profiles: List[GiddCountryListType] = strawberry.django.field()

    @strawberry.field
    def country_profile(self, pk: Optional[strawberry.ID] = None, iso3: Optional[str] = None) -> GiddCountryType:
        return get_country_object(pk, iso3)
