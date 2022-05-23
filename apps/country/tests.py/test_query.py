
import pytest
from config.schema import schema
from asgiref.sync import sync_to_async

from apps.country.factories import CountryFactory


pytestmark = pytest.mark.asyncio


@sync_to_async
def create_country():
    return CountryFactory()


@pytest.mark.django_db
@pytest.mark.asyncio
async def test_query():
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
    single_country_query = """
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

    country1 = await create_country()
    country1_id = country1.id
    await create_country()
    countries_result = await schema.execute(countries_query)
    assert countries_result.errors is None
    assert len(countries_result.data['countries']) == 2

    single_country_result = await schema.execute(single_country_query, variable_values={"pk": str(country1_id)},)
    assert str(country1_id) == single_country_result.data['country']['id']
