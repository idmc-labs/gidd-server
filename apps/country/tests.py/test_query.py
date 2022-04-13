
import pytest
from config.schema import schema


@pytest.mark.django_db
def test_query():
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
                countryAdditonalInfo {
                id
                totalDisplacement
                totalDisplacementSince
                totalDisplacementSource
                year
                }
            }
        }
    """
    # single_country_query = """
    #     query MyQuery($id: ID!) {
    #         country(id: $id) {
    #             id
    #             idmcContinent
    #             idmcNames
    #             idmcRegion
    #             idmcSubRegion
    #             isConflictAffectedSince1970
    #             isCountryOfficeIom
    #             isCountryOfficeNrc
    #             isIdmcGo2013
    #             isLeastDevelopedCountry
    #             isSmallIslandDevelopingState
    #             iso2
    #             iso3
    #             name
    #             unPopulationDivisionNames
    #             unitedNationsRegion
    #             wbRegion
    #             countryAdditonalInfo {
    #             id
    #             totalDisplacement
    #             totalDisplacementSince
    #             totalDisplacementSource
    #             year
    #             }
    #         }
    #     }
    # """

    counrtries_result = schema.execute(countries_query)
    print(counrtries_result)

    # assert counrtries_result.errors is None
    # assert result.data["books"] == [
    #     {
    #         "title": "The Great Gatsby",
    #         "author": "F. Scott Fitzgerald",
    #     }
    # ]