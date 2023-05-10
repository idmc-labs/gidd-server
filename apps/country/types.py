# types.py
import strawberry
from strawberry import auto
import strawberry_django
from .models import (
    Country,
    CountryAdditionalInfo,
    OverView,
)
from .gh_filters import (
    CountryFilter,
    CountryAdditionalInfoFilter,
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
from utils import FileFieldType, build_url, get_enum_label


@strawberry.django.type(OverView, pagination=True)
class GiddOverViewType:
    id: auto
    description: auto
    year: auto
    updated_at: auto


@strawberry.django.type(CountryAdditionalInfo, pagination=True, filters=CountryAdditionalInfoFilter)
class GiddCountryAdditionalInfoType:
    id: auto
    year: auto
    total_displacement: auto
    total_displacement_since: auto
    total_displacement_source: auto


@strawberry.django.type(CountryAdditionalInfo, pagination=True, filters=CountryAdditionalInfoFilter)
class GiddCountryAdditionalInfoListType(GiddCountryAdditionalInfoType):
    pass


@strawberry.django.type(Country)
class GiddCountryType:
    id: auto
    iso3: auto
    iso2: auto
    name: auto
    idmc_names: auto
    idmc_continent: ContinentEnum
    idmc_region: IdmcRegionEnum
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
    async def country_additonal_info(self, info: Info) -> List[GiddCountryAdditionalInfoType]:
        return await info.context["country_additonal_loader"].load(self.id)

    @strawberry.field
    async def overviews(self, info: Info) -> List[GiddOverViewType]:
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
        return get_enum_label(ContinentEnum, self.idmc_continent)

    @strawberry.field
    async def idmc_region_label(self, info: Info) -> str:
        return get_enum_label(IdmcRegionEnum, self.idmc_region)

    @strawberry.field
    async def idmc_sub_region_label(self, info: Info) -> str:
        return get_enum_label(SubRegionEnum, self.idmc_sub_region)

    @strawberry.field
    async def wb_region_label(self, info: Info) -> str:
        return get_enum_label(WbRegionEnum, self.wb_region)

    @strawberry.field
    async def good_practice_region_label(self, info: Info) -> str:
        return get_enum_label(GoodPracticeRegionEnum, self.good_practice_region)

    @strawberry.field
    async def united_nations_region_label(self, info: Info) -> str:
        return get_enum_label(UnitedNationsRegionEnum, self.united_nations_region)


@strawberry.django.type(Country, pagination=True, filters=CountryFilter)
class GiddCountryListType(GiddCountryType):
    pass


@strawberry_django.input(CountryAdditionalInfo)
class GiddCountryAdditionalInfoInputType:
    year: auto
    total_displacement: auto
    total_displacement_since: auto
    total_displacement_source: auto
