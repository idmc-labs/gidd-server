# types.py
import strawberry
from strawberry import auto, ID
import strawberry_django
from .models import (
    Country,
    CountryAdditionalInfo,
    Conflict,
    Disaster,
    OverView,
)
from .gh_filters import (
    CountryFilter,
    CountryAdditionalInfoFilter,
    ConflictFilter,
    DisasterFilter,
)
from typing import List, Optional
from strawberry.types import Info
from .enums import (
    ContinentEnum,
    IdmcRegionEnum,
    WbRegionEnum,
    UnitedNationsRegionEnum,
    SubRegionEnum,
    GoodPracticeRegionEnum,
)
from utils import FileFieldType, build_url


@strawberry.django.type(OverView, pagination=True)
class OverViewType:
    id: auto
    description: auto
    year: auto
    updated_at: auto


@strawberry.django.type(CountryAdditionalInfo, pagination=True, filters=CountryAdditionalInfoFilter)
class CountryAdditionalInfoType:
    id: auto
    year: auto
    total_displacement: auto
    total_displacement_since: auto
    total_displacement_source: auto


@strawberry.django.type(CountryAdditionalInfo, pagination=True, filters=CountryAdditionalInfoFilter)
class CountryAdditionalInfoListType(CountryAdditionalInfoType):
    pass


@strawberry.type
class TimeSeriesStatisticsType:
    year: str
    total: int


@strawberry.type
class DisasterCountryType:
    id: ID
    iso3: str
    country_name: str


@strawberry.type
class DisasterTimeSeriesStatisticsType:
    year: str
    total: int
    country: DisasterCountryType


@strawberry.type
class CategoryStatisticsType:
    label: str
    total: int


@strawberry.type
class ConflictStatisticsType:
    new_displacements: int
    total_idps: int
    new_displacement_timeseries: List[TimeSeriesStatisticsType]
    idps_timeseries: List[TimeSeriesStatisticsType]


@strawberry.type
class DisasterStatisticsType:
    new_displacements: int
    total_events: int
    timeseries: List[DisasterTimeSeriesStatisticsType]
    categories: List[CategoryStatisticsType]


@strawberry.django.type(Country)
class CountryType:
    id: auto
    iso3: auto
    iso2: auto
    name: auto
    idmc_names: auto
    idmc_continent: ContinentEnum
    idmc_region:IdmcRegionEnum
    idmc_sub_region: SubRegionEnum
    wb_region: WbRegionEnum
    good_practice_region: GoodPracticeRegionEnum
    un_population_division_names: auto
    united_nations_region: UnitedNationsRegionEnum
    is_least_developed_country: auto
    is_small_island_developing_state: auto
    is_idmc_go_2013: auto
    is_conflict_affected_since_1970: auto
    is_country_office_nrc: auto
    is_country_office_iom: auto
    title: auto
    description: auto
    essential_links: auto
    contact_person_description: auto
    internal_displacement_description: auto
    displacement_data_description: auto
    bounding_box: List[float]
    center_point: List[float]

    @strawberry.field
    async def country_additonal_info(self, info: Info) -> List[CountryAdditionalInfoType]:
        return await info.context["country_additonal_loader"].load(self.id)

    @strawberry.field
    async def overviews(self, info: Info) -> List[OverViewType]:
        return await info.context["country_overviews_loader"].load(self.id)

    @strawberry.field
    async def background_image(self, info: Info) -> Optional[FileFieldType]:
        return build_url(self.background_image, info.context['request'])

    @strawberry.field
    async def contact_person_image(self, info: Info) -> Optional[FileFieldType]:
        return build_url(self.contact_person_image, info.context['request'])

    @strawberry.field
    async def good_practices_count(self, info: Info) -> Optional[int]:
        return await info.context["country_good_practice_loader"].load(self.id)

    @strawberry.field
    async def idmc_continent_label(self, info: Info) -> Optional[str]:
        return ContinentEnum(self.idmc_continent).label if self.idmc_continent else ""

    @strawberry.field
    async def idmc_region_label(self, info: Info) -> str:
        return IdmcRegionEnum(self.idmc_region).label if self.idmc_region else ""

    @strawberry.field
    async def idmc_sub_region_label(self, info: Info) -> str:
        return SubRegionEnum(self.idmc_sub_region).label if self.idmc_sub_region else ""

    @strawberry.field
    async def wb_region_label(self, info: Info) -> str:
        return WbRegionEnum(self.wb_region).label if self.wb_region else ""

    @strawberry.field
    async def good_practice_region_label(self, info: Info) -> str:
        return GoodPracticeRegionEnum(self.good_practice_region).label if self.good_practice_region else ""

    @strawberry.field
    async def united_nations_region_label(self, info: Info) -> str:
        return UnitedNationsRegionEnum(self.united_nations_region).label if self.united_nations_region else ""


@strawberry.django.type(Country, pagination=True, filters=CountryFilter)
class CountryListType(CountryType):
    pass


@strawberry.django.type(Conflict)
class ConflictType:
    id: auto
    year: auto
    total_displacement: auto
    total_displacement_source: auto
    new_displacement: auto
    new_displacement_source: auto
    returns: auto
    returns_source: auto
    local_integration: auto
    local_integration_source: auto
    resettlement: auto
    resettlement_source: auto
    cross_border_flight: auto
    cross_border_flight_source: auto
    children_born_to_idps: auto
    children_born_to_idps_source: auto
    idp_deaths: auto
    idp_deaths_source: auto
    total_displacement_since: auto
    new_displacement_since: auto
    returns_since: auto
    resettlement_since: auto
    local_integration_since: auto
    cross_border_flight_since: auto
    children_born_to_idps_since: auto
    idp_deaths_since: auto
    country: CountryListType


@strawberry.django.type(Conflict, pagination=True, filters=ConflictFilter)
class ConflictListType(ConflictType):
    pass


@strawberry.django.type(Disaster)
class DisasterType:
    id: auto
    year: auto
    glide_number: auto
    event_name: auto
    location_text: auto
    start_date: auto
    start_date_accuracy: auto
    end_date: auto
    end_date_accuracy: auto
    hazard_category: auto
    hazard_sub_category: auto
    hazard_sub_type: auto
    hazard_type: auto
    new_displacement: auto
    new_displacement_source: auto
    new_displacement_since: auto
    country: CountryListType


@strawberry.django.type(Disaster, pagination=True, filters=DisasterFilter)
class DisasterListType(DisasterType):
    pass


@strawberry_django.input(CountryAdditionalInfo)
class CountryAdditionalInfoInputType:
    year: auto
    total_displacement: auto
    total_displacement_since: auto
    total_displacement_source: auto


@strawberry_django.input(Country)
class CountryInputType:
    iso3: auto
    iso2: auto
    name: auto
    idmc_names: auto
    idmc_continent: auto
    idmc_region: IdmcRegionEnum
    idmc_sub_region: auto
    wb_region: auto
    un_population_division_names: auto
    united_nations_region: auto
    is_least_developed_country: auto
    is_small_island_developing_state: auto
    is_idmc_go_2013: auto
    is_conflict_affected_since_1970: auto
    is_country_office_nrc: auto
    is_country_office_iom: auto


@strawberry_django.input(Conflict)
class ConflictInputType:
    year: auto
    total_displacement: auto
    total_displacement_source: auto
    new_displacement: auto
    new_displacement_source: auto
    returns: auto
    returns_source: auto
    local_integration: auto
    local_integration_source: auto
    resettlement: auto
    resettlement_source: auto
    cross_border_flight: auto
    cross_border_flight_source: auto
    children_born_to_idps: auto
    children_born_to_idps_source: auto
    idp_deaths: auto
    idp_deaths_source: auto
    total_displacement_since: auto
    new_displacement_since: auto
    returns_since: auto
    resettlement_since: auto
    local_integration_since: auto
    cross_border_flight_since: auto
    children_born_to_idps_since: auto
    idp_deaths_since: auto
    country: CountryInputType
