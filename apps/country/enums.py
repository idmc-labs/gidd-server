import strawberry
from .models import Country, FigureAnalysis

ContinentEnum = strawberry.enum(Country.Continent, name="ContinentEnum")
IdmcRegionEnum = strawberry.enum(Country.IdmcRegion, name="IdmcRegionEnum")
WbRegionEnum = strawberry.enum(Country.WbRegion, name="WbRegionEnum")
UnitedNationsRegionEnum = strawberry.enum(Country.UnitedNationsRegion, name="UnitedNationsRegionEnum")
SubRegionEnum = strawberry.enum(Country.SubRegion, name="SubRegionEnum")
GoodPracticeRegionEnum = strawberry.enum(Country.GoodPracticeRegion, name="GoodPracticeRegion")
CrisisTypeEnum = strawberry.enum(FigureAnalysis.CrisisType, name="CrisisType")
