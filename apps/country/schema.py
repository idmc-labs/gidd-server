import strawberry
from typing import List
from .types import (
    ConflictType,
    DisasterType,
    CountryType,
    ConflictListType,
    DisasterListType,
    CountryListType,
)


@strawberry.type
class Query:
    conflicts: List[ConflictListType] = strawberry.django.field()
    disasters: List[DisasterListType] = strawberry.django.field()
    countries: List[CountryListType] = strawberry.django.field()
    conflict: ConflictType = strawberry.django.field()
    disaster: DisasterType = strawberry.django.field()
    country: CountryType = strawberry.django.field()
