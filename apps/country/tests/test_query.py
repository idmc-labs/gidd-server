from apps.country.factories import CountryFactory
from config.tests import TestCase


class CountryQueryTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.country1 = CountryFactory.create()

    def test_country_query(self):
        query = """
            query MyQuery($pk: ID!) {
                country(pk: $pk) {
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
                    unitedNationsRegion
                    wbRegion
                }
            }
        """
        country1 = self.country1
        resp = self.query_check(query, variables={'pk': str(country1.pk)})
        assert str(country1.id) == resp['data']['country']['id']

    def test_countries_query(self):
        countries_query = """
            query MyQuery {
                countries {
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
                    unitedNationsRegion
                    wbRegion
                    idmcContinent
                }
            }
        """
        CountryFactory.create()  # Create another one
        resp = self.query_check(countries_query)
        assert len(resp['data']['countries']) == 2
