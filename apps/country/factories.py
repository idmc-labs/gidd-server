
import factory
from factory import fuzzy
from factory.django import DjangoModelFactory

from .models import Country, CountryAdditionalInfo


class CountryFactory(DjangoModelFactory):
    name = fuzzy.FuzzyText(length=15)
    iso3 = fuzzy.FuzzyText(length=5)
    iso2 = fuzzy.FuzzyText(length=5)
    idmc_names = fuzzy.FuzzyText(length=15)
    idmc_continent = Country.Continent.EUROPE.value
    idmc_region = Country.Region.SOUTH_EAST_ASIA.value
    idmc_sub_region = Country.SubRegion.CARIBBEAN.value
    wb_region = Country.Region.SOUTHERN_EUROPE.value
    un_population_division_names = fuzzy.FuzzyText(length=5)
    united_nations_region = Country.Region.SOUTH_EAST_ASIA.value
    is_least_developed_country = True
    is_small_island_developing_state = True
    is_idmc_go_2013 = False
    is_conflict_affected_since_1970 = True
    is_country_office_nrc = True
    is_country_office_iom = True

    class Meta:
        model = Country


class CountryAdditionalInfoFactory(DjangoModelFactory):
    country = factory.SubFactory(CountryFactory)
    year = fuzzy.FuzzyInteger(2000, 2050)
    total_displacement = fuzzy.FuzzyInteger(100000, 200000)
    total_displacement_since = fuzzy.FuzzyInteger(10000, 30000)
    total_displacement_source = fuzzy.FuzzyText(length=15)

    class Meta:
        model = CountryAdditionalInfo
