# types.py
import strawberry
from strawberry.django import auto
import strawberry_django
from .models import (
    Country,
    CountryAdditionalInfo,
    Conflict,
    Disaster,
    OverView,
    EssentialLink,
    ContactPerson,
)
from .gh_filters import (
    CountryFilter,
    CountryAdditionalInfoFilter,
    ConflictFilter,
    DisasterFilter,
)
from typing import List
from strawberry.types import Info
from .enums import (
    ContinentEnum,
    RegionEnum,
    SubRegionEnum,
)
from utils import FileFieldType, build_url


@strawberry.django.type(OverView, pagination=True)
class OverViewType:
    id: auto
    description: auto
    year: auto
    updated_at: auto


@strawberry.django.type(EssentialLink, pagination=True)
class EssentialLinkType:
    id: auto
    link: auto
    title: auto


@strawberry.django.type(ContactPerson, pagination=True)
class ContactPersonType:
    id: auto
    full_name: auto
    email: auto
    designation: auto

    @strawberry.field
    async def image(self, info: Info) -> FileFieldType:
        return build_url(self.image, info.context['request'])


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


@strawberry.django.type(Country)
class CountryType:
    id: auto
    iso3: auto
    iso2: auto
    name: auto
    idmc_names: auto
    idmc_continent: ContinentEnum
    idmc_region: RegionEnum
    idmc_sub_region: SubRegionEnum
    wb_region: RegionEnum
    un_population_division_names: auto
    united_nations_region: RegionEnum
    is_least_developed_country: auto
    is_small_island_developing_state: auto
    is_idmc_go_2013: auto
    is_conflict_affected_since_1970: auto
    is_country_office_nrc: auto
    is_country_office_iom: auto
    title: auto
    description: auto

    @strawberry.field
    async def country_additonal_info(self, info: Info) -> List[CountryAdditionalInfoType]:
        return await info.context["country_additonal_loader"].load(self.id)

    @strawberry.field
    async def overviews(self, info: Info) -> List[OverViewType]:
        return await info.context["country_overviews_loader"].load(self.id)

    @strawberry.field
    async def essential_links(self, info: Info) -> List[EssentialLinkType]:
        return await info.context["country_essential_links_loader"].load(self.id)

    @strawberry.field
    async def contact_persons(self, info: Info) -> List[ContactPersonType]:
        return await info.context["country_contact_persons_loader"].load(self.id)

    @strawberry.field
    async def background_image(self, info: Info) -> FileFieldType:
        return build_url(self.background_image, info.context['request'])


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
    idmc_region: RegionEnum
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
