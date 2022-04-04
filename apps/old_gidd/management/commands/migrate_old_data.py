from django.core.management.base import BaseCommand
from apps.country.models import (
    Country as NewCountry,
    CountryAdditionalInfo,
    Conflict as NewConflict,
    Disaster as NewDisaster,
)

from apps.old_gidd.models import (
    Country as OldCountry,
    CountryDisasterInfo,
    Conflict as OldConflict,
    Disaster as OldDisaster,
)


class Command(BaseCommand):
    help = 'Migrate old gidd data to new'

    def _clean_country_enum(self, enum_value):
        if enum_value == 'western_euope':
            enum_value = 'western_europe'
        if enum_value in ['', 'NA']:
            return None
        return enum_value.strip().replace(",", "").replace("-", "_").replace(" ", "_").lower()

    def _country_continent_enum_map(self, enum_value):
        cleaned_enum_value = self._clean_country_enum(enum_value)
        if cleaned_enum_value:
            return NewCountry.Region(
                cleaned_enum_value
            )
        return None

    def _country_region_enum_map(self, enum_value):
        cleaned_enum_value = self._clean_country_enum(enum_value)
        if cleaned_enum_value:
            return NewCountry.Region(
                self._clean_country_enum(cleaned_enum_value)
            )
        return None

    def _country_subregion_enum_map(self, enum_value):
        cleaned_enum_value = self._clean_country_enum(enum_value)
        if cleaned_enum_value:
            return NewCountry.SubRegion(
                self._clean_country_enum(cleaned_enum_value)
            )
        return None

    def reset_new_db(self):
        NewDisaster.objects.all().delete()
        NewConflict.objects.all().delete()
        CountryAdditionalInfo.objects.all().delete()
        NewCountry.objects.all().delete()

    def get_country_id_from_iso3(self, iso3):
        try:
            return NewCountry.objects.get(iso3=iso3).id
        except NewCountry.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'for {iso3} ISO3 country does not exists \n'))
            return NewCountry.objects.create(iso3=iso3, name=f'{iso3} (This iso3 have no country)').id

    def create_countries(self):
        NewCountry.objects.bulk_create(
            [
                NewCountry(
                    iso3=old_country.iso3,
                    iso2=old_country.iso2,
                    name=old_country.idmc_names,
                    idmc_names=old_country.idmc_names,
                    idmc_continent=self._country_continent_enum_map(old_country.idmc_continent),
                    idmc_region=self._country_region_enum_map(old_country.idmc_region),
                    idmc_sub_region=self._country_subregion_enum_map(old_country.idmc_sub_region),
                    wb_region=self._country_region_enum_map(old_country.wb_region),
                    un_population_division_names=old_country.un_population_division_names,
                    united_nations_region=self._country_region_enum_map(old_country.united_nations_region),
                    is_least_developed_country=old_country.least_developed_countries,
                    is_small_island_developing_state=old_country.small_island_developing_states,
                    is_idmc_go_2013=old_country.idmc_go_2013,
                    is_conflict_affected_since_1970=old_country.conflict_affected_since_1970,
                    is_country_office_nrc=old_country.country_office_nrc,
                    is_country_office_iom=old_country.country_office_iom,
                ) for old_country in OldCountry.objects.using('idmc_public').all()
            ]
        )
        self.stdout.write(self.style.SUCCESS(f'{NewCountry.objects.count()} Countries created. \n'))

    def create_countries_addtional_info(self):
        CountryAdditionalInfo.objects.bulk_create(
            [
                CountryAdditionalInfo(
                    country_id=self.get_country_id_from_iso3(country_disaster_info['iso3']),
                    year=country_disaster_info['year'],
                    total_displacement=country_disaster_info['total_displacement'],
                    total_displacement_since=country_disaster_info['total_displacement_since'],
                    total_displacement_source=country_disaster_info['total_displacement_source'],
                ) for country_disaster_info in CountryDisasterInfo.objects.using('idmc_platform').values(
                    'iso3', 'total_displacement', 'total_displacement_since', 'total_displacement_source', 'year'
                )
            ]
        )
        self.stdout.write(self.style.SUCCESS(
            f'{CountryAdditionalInfo.objects.count()} Countries additional info created.\n')
        )

    def create_conflicts(self):
        NewConflict.objects.bulk_create(
            [
                NewConflict(
                    country_id=self.get_country_id_from_iso3(old_conflict.iso3),
                    year=old_conflict.year,
                    total_displacement=old_conflict.total_displacement,
                    total_displacement_source=old_conflict.total_displacement_source,
                    new_displacement=old_conflict.new_displacement,
                    new_displacement_source=old_conflict.new_displacement_source,
                    returns=old_conflict.returns,
                    returns_source=old_conflict.returns_source,
                    local_integration=old_conflict.local_integration,
                    local_integration_source=old_conflict.local_integration_source,
                    resettlement=old_conflict.resettlement,
                    resettlement_source=old_conflict.resettlement_source,
                    cross_border_flight=old_conflict.cross_border_flight,
                    cross_border_flight_source=old_conflict.cross_border_flight_source,
                    children_born_to_idps=old_conflict.children_born_to_idps,
                    children_born_to_idps_source=old_conflict.children_born_to_idps_source,
                    idp_deaths=old_conflict.idp_deaths,
                    idp_deaths_source=old_conflict.idp_deaths_source,
                    total_displacement_since=old_conflict.total_displacement_since,
                    new_displacement_since=old_conflict.new_displacement_since,
                    returns_since=old_conflict.returns_since,
                    resettlement_since=old_conflict.resettlement_since,
                    local_integration_since=old_conflict.local_integration_since,
                    cross_border_flight_since=old_conflict.cross_border_flight_since,
                    children_born_to_idps_since=old_conflict.children_born_to_idps_since,
                    idp_deaths_since=old_conflict.idp_deaths_since,
                ) for old_conflict in OldConflict.objects.using('idmc_platform').all()
            ]
        )
        self.stdout.write(self.style.SUCCESS(f'{NewConflict.objects.count()} conflicts created.\n'))

    def create_disasters(self):
        NewDisaster.objects.bulk_create(
            [
                NewDisaster(
                    country_id=self.get_country_id_from_iso3(old_disaster.iso3),
                    year=old_disaster.year,
                    glide_number=old_disaster.glide_number,
                    event_name=old_disaster.event_name,
                    location_text=old_disaster.location_text,
                    start_date=old_disaster.start_date,
                    start_date_accuracy=old_disaster.start_date_accuracy,
                    end_date=old_disaster.end_date,
                    end_date_accuracy=old_disaster.end_date_accuracy,
                    hazard_category=old_disaster.hazard_category,
                    hazard_sub_category=old_disaster.hazard_sub_category,
                    hazard_sub_type=old_disaster.hazard_sub_type,
                    hazard_type=old_disaster.hazard_type,
                    new_displacement=old_disaster.new_displacement,
                    new_displacement_source=old_disaster.new_displacement_source,
                    new_displacement_since=old_disaster.new_displacement_since,
                ) for old_disaster in OldDisaster.objects.using('idmc_platform').all()
            ]
        )
        self.stdout.write(self.style.SUCCESS(f'{NewDisaster.objects.count()} disasters created.\n'))

    def handle(self, *args, **options):
        self.reset_new_db()
        self.create_countries()
        self.create_countries_addtional_info()
        self.create_conflicts()
        self.create_disasters()
