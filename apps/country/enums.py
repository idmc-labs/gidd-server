from strawberry.enum import _process_enum
from .models import Country

ContinentEnum = _process_enum(Country.Continent, "ContinentEnum", "Continent enum")
IdmcRegionEnum = _process_enum(Country.IdmcRegion, "IdmcRegionEnum", "idmc country regions")
WbRegionEnum = _process_enum(Country.WbRegion, "WbRegionEnum", "wb country regions")
UnitedNationsRegionEnum = _process_enum(
    Country.UnitedNationsRegion, "UnitedNationsRegionEnum", "united nations country regions"
)
SubRegionEnum = _process_enum(Country.SubRegion, "SubRegionEnum", "country sub regions")
GoodPracticeRegionEnum = _process_enum(Country.GoodPracticeRegion, "GoodPracticeRegion", "good practice regions")
