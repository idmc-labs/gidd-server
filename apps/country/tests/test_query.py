from django.utils import translation

from apps.country.models import Country
from apps.country.factories import CountryFactory
from config.tests import TestCase


class CountryQueryTestCase(TestCase):
    COUNTRY_QUERY = """
        query MyQuery($pk: ID!) {
            countryProfile(pk: $pk) {
                id
                idmcContinent
                idmcNames
                idmcRegion
                idmcSubRegion
                isConflictAffectedSince1970
                isCountryOfficeIom
                isCountryOfficeNrc
                isIdmcGo2013
                isLeastDevelopedCountry
                isSmallIslandDevelopingState
                iso2
                iso3
                name
                unPopulationDivisionNames
            }
        }
    """

    COUNTRIES_QUERY = """
        query MyQuery {
            countryProfiles {
                id
                idmcNames
                idmcRegion
                idmcSubRegion
                isConflictAffectedSince1970
                isCountryOfficeIom
                isCountryOfficeNrc
                isIdmcGo2013
                isLeastDevelopedCountry
                isSmallIslandDevelopingState
                iso3
                iso2
                name
                unPopulationDivisionNames
                idmcContinent
            }
        }
    """

    @staticmethod
    def _get_country_in_response_format(country: Country):
        return dict(
            id=str(country.id),
            idmcNames=country.idmc_names,
            idmcContinent=Country.Continent(country.idmc_continent).name,
            idmcRegion=Country.IdmcRegion(country.idmc_region).name,
            idmcSubRegion=Country.IdmcRegion(country.idmc_sub_region).name,
            isConflictAffectedSince1970=country.is_conflict_affected_since_1970,
            isCountryOfficeIom=country.is_country_office_iom,
            isCountryOfficeNrc=country.is_country_office_nrc,
            isIdmcGo2013=country.is_idmc_go_2013,
            isLeastDevelopedCountry=country.is_least_developed_country,
            isSmallIslandDevelopingState=country.is_small_island_developing_state,
            iso2=country.iso2,
            iso3=country.iso3,
            name=country.name,
            unPopulationDivisionNames=country.un_population_division_names,
        )

    @classmethod
    def setUpTestData(cls):
        cls.countries = CountryFactory.create_batch(3)

    def test_country_query(self):
        country = self.countries[0]
        for lang in self.TEST_LANGUAGES:
            resp = self.query_check(self.COUNTRY_QUERY, variables={'pk': str(country.pk)}, HTTP_ACCEPT_LANGUAGE=lang)
            with translation.override(lang):
                assert self._get_country_in_response_format(country) == resp['data']['countryProfile']
                assert str(country.id) == resp['data']['countryProfile']['id']

    def test_countries_query(self):
        countries = self.countries
        for lang in self.TEST_LANGUAGES:
            resp = self.query_check(self.COUNTRIES_QUERY, HTTP_ACCEPT_LANGUAGE=lang)
            with translation.override(lang):
                assert [
                    self._get_country_in_response_format(country)
                    for country in countries
                ] == resp['data']['countryProfiles']
