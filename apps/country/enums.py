from strawberry.enum import _process_enum
from .models import Country

ContinentEnum = _process_enum(Country.Continent, "ContinentEnum", "Continent enum")
RegionEnum = _process_enum(Country.Region, "RegionEnum", "country regions")
SubRegionEnum = _process_enum(Country.SubRegion, "SubRegionEnum", "country sub regions")
GoodPracticeRegionEnum = _process_enum(Country.GoodPracticeRegion, "GoodPracticeRegion", "good practice regions")
