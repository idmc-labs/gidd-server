import strawberry
from strawberry_django import mutations

from .types import (
    CountryType,
    CountryInputType,
    ConflictType,
    ConflictInputType,
)


@strawberry.type
class Mutation:
    createCountry: CountryType = mutations.create(CountryInputType)
    createConflict: ConflictType = mutations.create(ConflictInputType)
