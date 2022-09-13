from django.core.management.base import BaseCommand
import csv
import os
from django.conf import settings
from django.db.models import Q
from django.utils import timezone
from apps.country.models import (
    Country as NewCountry,
    CountryAdditionalInfo,
    Conflict as NewConflict,
    Disaster as NewDisaster,
    SnapshotFile,
)

from apps.old_gidd.models import (
    Country as OldCountry,
    CountryDisasterInfo,
    Conflict as OldConflict,
    Disaster as OldDisaster,
)
from .country_bounding import COUNTRY_BOUNDING
from django.core.files.base import File


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

    def _country_idmc_region_enum_map(self, enum_value):
        cleaned_enum_value = self._clean_country_enum(enum_value)
        if cleaned_enum_value:
            return NewCountry.IdmcRegion(
                self._clean_country_enum(cleaned_enum_value)
            )
        return None

    def _country_wb_region_enum_map(self, enum_value):
        cleaned_enum_value = self._clean_country_enum(enum_value)
        if cleaned_enum_value:
            return NewCountry.WbRegion(
                self._clean_country_enum(cleaned_enum_value)
            )
        return None

    def _country_united_nations_region_enum_map(self, enum_value):
        cleaned_enum_value = self._clean_country_enum(enum_value)
        if cleaned_enum_value:
            return NewCountry.UnitedNationsRegion(
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

    def get_country_id_from_iso3(self, iso3):
        try:
            return NewCountry.objects.get(iso3=iso3).id
        except NewCountry.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'for {iso3} ISO3 country does not exists \n'))
            return NewCountry.objects.create(iso3=iso3, name=f'{iso3} (This iso3 have no country)').id

    def _country_iso_to_bounding_box_map(self, iso3):
        for bound in COUNTRY_BOUNDING:
            if bound['iso3'] == iso3:
                return bound['bounding_box']

    def _capitalize_string(self, string):
        value = string.capitalize() if string else None
        if value == 'Volcanic eruption':
            value = 'Volcanic activity'
        return value

    def _get_contact_description_from_contact_list(self, iso3, contact_data):
        for contact in contact_data:
            if contact['ISO3'] == iso3:
                return f'''
                    <p>
                        Do you have more questions about this country? Contact
                        our Monitoring ExpertDo you have more questions about
                        this country? Contact our Monitoring Expert
                    </p>
                    <p>
                        <b>{contact['ME']}</b>
                    </p>
                    <p>
                        {contact['TITLE']}
                    </p>
                    <p>
                        <a href="mailto:{contact['EMAIL']}">📧 Email </a>
                    </p>
                '''

    def _get_figures_analysis_data(self, iso3, displacement_data):
        for displacement in displacement_data:
            if displacement[1] == iso3.lower():
                return f'''
                    <p>
                        Learn more about the sources of our figures, as well as
                        our methodologies and caveats.
                    </p>
                    <p>
                        <a href={displacement[0]}>🗎 Latest Figure Analysis (PDF)</a>
                    </p>
                '''

    def _get_country_descriptoin(self):
        return '''
            <p>
                Welcome to IDMC's country profile pages. Here, you will find key information
                and data on internal displacement at the country level. By using our intuitive
                navigation tools, you will be able to query and download our data, and get
                the latest updates on internal displacement. You will also find material
                related to the country in question, as well as essential reading and
                methodological documentation.
            </p>
        '''

    def _generate_country_addtional_info_snapshot_file(self, year):
        file_path = '/tmp/country_additional_info.csv'
        with open(file_path, mode='w') as file:
            writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow([
                'country_id', 'year', 'total_displacement',
                'total_displacement_since', 'total_displacement_source'
            ])
            for country_additonal_info in CountryAdditionalInfo.objects.filter(year=year):
                writer.writerow([
                    country_additonal_info.country_id,
                    country_additonal_info.year,
                    country_additonal_info.total_displacement,
                    country_additonal_info.total_displacement_since,
                    country_additonal_info.total_displacement_source,
                ])
            file.close()
        file = open(file_path)
        snaphot_file = SnapshotFile.objects.create(title=f'Country addtional info - {timezone.now()}')
        snaphot_file.snaphot_file.save('country addtional_info.csv', File(file))
        file.close()

    def _generate_conflict_snapshot_file(self, year):
        file_path = '/tmp/conflict.csv'
        with open(file_path, mode='w') as file:
            writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow([
                'country_id',
                'year',
                'total_displacement',
                'total_displacement_source',
                'new_displacement',
                'new_displacement_source',
                'returns',
                'returns_source',
                'local_integration',
                'local_integration_source',
                'resettlement',
                'resettlement_source',
                'cross_border_flight',
                'cross_border_flight_source',
                'children_born_to_idps',
                'children_born_to_idps_source',
                'idp_deaths',
                'idp_deaths_source',
                'total_displacement_since',
                'new_displacement_since',
                'returns_since',
                'resettlement_since',
                'local_integration_since',
                'cross_border_flight_since',
                'children_born_to_idps_since',
                'idp_deaths_since',
                'old_id',
            ])
            for conflict in NewConflict.objects.filter(year=year):
                writer.writerow([
                    conflict.country_id,
                    conflict.year,
                    conflict.total_displacement,
                    conflict.total_displacement_source,
                    conflict.new_displacement,
                    conflict.new_displacement_source,
                    conflict.returns,
                    conflict.returns_source,
                    conflict.local_integration,
                    conflict.local_integration_source,
                    conflict.resettlement,
                    conflict.resettlement_source,
                    conflict.cross_border_flight,
                    conflict.cross_border_flight_source,
                    conflict.children_born_to_idps,
                    conflict.children_born_to_idps_source,
                    conflict.idp_deaths,
                    conflict.idp_deaths_source,
                    conflict.total_displacement_since,
                    conflict.new_displacement_since,
                    conflict.returns_since,
                    conflict.resettlement_since,
                    conflict.local_integration_since,
                    conflict.cross_border_flight_since,
                    conflict.children_born_to_idps_since,
                    conflict.idp_deaths_since,
                    conflict.old_id,
                ])
            file.close()
        file = open(file_path)
        snaphot_file = SnapshotFile.objects.create(title=f'Conflict - {timezone.now()}')
        snaphot_file.snaphot_file.save('conflict.csv', File(file))
        file.close()

    def _generate_disaster_snapshot_file(self, year):
        file_path = '/tmp/disaster.csv'
        with open(file_path, mode='w') as file:
            writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow([
                'country_id',
                'year',
                'glide_number',
                'event_name',
                'location_text',
                'start_date',
                'start_date_accuracy',
                'end_date',
                'end_date_accuracy',
                'hazard_category',
                'hazard_sub_category',
                'hazard_sub_type',
                'hazard_type',
                'new_displacement',
                'new_displacement_source',
                'new_displacement_since',
                'old_id',
            ])
            for disaster in NewDisaster.objects.filter(year=year):
                writer.writerow([
                    disaster.country_id,
                    disaster.year,
                    disaster.glide_number,
                    disaster.event_name,
                    disaster.location_text,
                    disaster.start_date,
                    disaster.start_date_accuracy,
                    disaster.end_date,
                    disaster.end_date_accuracy,
                    disaster.hazard_category,
                    disaster.hazard_sub_category,
                    disaster.hazard_sub_type,
                    disaster.hazard_type,
                    disaster.new_displacement,
                    disaster.new_displacement_source,
                    disaster.new_displacement_since,
                    disaster.old_id,
                ])
            file.close()
        file = open(file_path)
        snaphot_file = SnapshotFile.objects.create(title=f'Disaster - {timezone.now()}')
        snaphot_file.snaphot_file.save('disaster.csv', File(file))
        file.close()

    def sync_countries(self, contact_data, figures_analysis_data):

        old_country_iso3_list = list(OldCountry.objects.using('idmc_public').values_list('iso3', flat=True))
        country_qs = NewCountry.objects.all()
        new_country_iso3_list = country_qs.values_list('iso3', flat=True)

        # Create countries
        new_countries_to_add_iso3_list = list(set(old_country_iso3_list) - set(new_country_iso3_list))
        countries_to_add = OldCountry.objects.using('idmc_public').filter(iso3__in=new_countries_to_add_iso3_list)
        country_created = NewCountry.objects.bulk_create(
            [
                NewCountry(
                    iso3=old_country.iso3,
                    iso2=old_country.iso2,
                    name=old_country.idmc_names,
                    idmc_names=old_country.idmc_names,
                    idmc_continent=self._country_continent_enum_map(old_country.idmc_continent),
                    idmc_region=self._country_idmc_region_enum_map(old_country.idmc_region),
                    idmc_sub_region=self._country_subregion_enum_map(old_country.idmc_sub_region),
                    wb_region=self._country_wb_region_enum_map(old_country.wb_region),
                    un_population_division_names=old_country.un_population_division_names,
                    united_nations_region=self._country_united_nations_region_enum_map(old_country.united_nations_region),
                    is_least_developed_country=old_country.least_developed_countries,
                    is_small_island_developing_state=old_country.small_island_developing_states,
                    is_idmc_go_2013=old_country.idmc_go_2013,
                    is_conflict_affected_since_1970=old_country.conflict_affected_since_1970,
                    is_country_office_nrc=old_country.country_office_nrc,
                    is_country_office_iom=old_country.country_office_iom,
                    bounding_box=self._country_iso_to_bounding_box_map(old_country.iso3),
                    displacement_data_description=self._get_figures_analysis_data(
                        old_country.iso3, figures_analysis_data
                    ),
                    contact_person_description=self._get_contact_description_from_contact_list(
                        old_country.iso3, contact_data
                    ),
                ) for old_country in countries_to_add
            ]
        )
        self.stdout.write(self.style.SUCCESS(f'{len(country_created)} Countries created.'))

        # Update countries
        countries_to_update_qs = country_qs.filter(
            Q(iso3__in=old_country_iso3_list) & ~Q(iso3__in=new_countries_to_add_iso3_list)
        )
        for country in countries_to_update_qs:
            old_country = OldCountry.objects.using('idmc_public').get(iso3=country.iso3)
            country.iso3 = old_country.iso3
            country.iso2 = old_country.iso2
            country.name = old_country.idmc_names
            country.idmc_names = old_country.idmc_names
            country.idmc_continent = self._country_continent_enum_map(old_country.idmc_continent)
            country.idmc_region = self._country_region_enum_map(old_country.idmc_region)
            country.idmc_sub_region = self._country_subregion_enum_map(old_country.idmc_sub_region)
            country.wb_region = self._country_region_enum_map(old_country.wb_region)
            country.un_population_division_names = old_country.un_population_division_names
            country.united_nations_region = self._country_region_enum_map(old_country.united_nations_region)
            country.is_least_developed_country = old_country.least_developed_countries
            country.is_small_island_developing_state = old_country.small_island_developing_states
            country.is_idmc_go_2013 = old_country.idmc_go_2013
            country.is_conflict_affected_since_1970 = old_country.conflict_affected_since_1970
            country.is_country_office_nrc = old_country.country_office_nrc
            country.is_country_office_iom = old_country.country_office_iom
            country.save()
        self.stdout.write(self.style.SUCCESS(f'{countries_to_update_qs.count()} Countries updated. \n'))

    def sync_countries_addtional_info(self, year):
        # Create current snapshoot file and save
        self._generate_country_addtional_info_snapshot_file(year)

        old_country_addtional_info_iso3_list = list(
            CountryDisasterInfo.objects.using('idmc_platform').filter(year=year).values_list('iso3', flat=True)
        )
        country_additonal_info_qs = CountryAdditionalInfo.objects.filter(year=year)
        new_country_addtional_info_iso3_list = country_additonal_info_qs.values_list('country__iso3', flat=True)

        # Remove country addtional info
        country_addtional_info_to_remove_qs = country_additonal_info_qs.filter(
            ~Q(country__iso3__in=old_country_addtional_info_iso3_list, year=year)
        )
        self.stdout.write(self.style.SUCCESS(
            f'{country_addtional_info_to_remove_qs.count()} Countries additional info deleted.')
        )
        country_addtional_info_to_remove_qs.delete()

        # Create country additional infos
        new_countries_addtional_info_to_add_iso3_list = list(
            set(old_country_addtional_info_iso3_list) - set(new_country_addtional_info_iso3_list)
        )
        countries_addtional_info_to_add = CountryDisasterInfo.objects.using('idmc_platform').filter(
            iso3__in=new_countries_addtional_info_to_add_iso3_list, year=year
        ).values(
            'iso3', 'total_displacement', 'total_displacement_since', 'total_displacement_source', 'year'
        )
        country_additonal_info_created = CountryAdditionalInfo.objects.bulk_create(
            [
                CountryAdditionalInfo(
                    country_id=self.get_country_id_from_iso3(country_disaster_info['iso3']),
                    year=country_disaster_info['year'],
                    total_displacement=country_disaster_info['total_displacement'],
                    total_displacement_since=country_disaster_info['total_displacement_since'],
                    total_displacement_source=country_disaster_info['total_displacement_source'],
                ) for country_disaster_info in countries_addtional_info_to_add
            ]
        )
        self.stdout.write(self.style.SUCCESS(
            f'{len(country_additonal_info_created)} Countries additional info created.')
        )

        # Update country addtional info
        countries_addtional_info_to_update_qs = country_additonal_info_qs.filter(
            Q(country__iso3__in=old_country_addtional_info_iso3_list) &
            Q(year=year) &
            ~Q(country__iso3__in=new_countries_addtional_info_to_add_iso3_list)
        ).values(
            'country__iso3', 'total_displacement', 'total_displacement_since', 'total_displacement_source'
        )
        countries_addtional_info_updated = 0
        for country_additonal_info in countries_addtional_info_to_update_qs:
            country_additonal_info_obj = CountryAdditionalInfo.objects.get(
                year=year, country__iso3=country_additonal_info['country__iso3']
            )
            old_country_additonal_info = CountryDisasterInfo.objects.using('idmc_platform').filter(
                year=year, iso3=country_additonal_info['country__iso3']
            ).values('total_displacement', 'total_displacement_since', 'total_displacement_source')[0]
            country_additonal_info_obj.total_displacement = old_country_additonal_info['total_displacement']
            country_additonal_info_obj.total_displacement_since = old_country_additonal_info['total_displacement_since']
            country_additonal_info_obj.total_displacement_source = old_country_additonal_info['total_displacement_source']
            country_additonal_info_obj.save()
            countries_addtional_info_updated += 1
        self.stdout.write(self.style.SUCCESS(
            f'{countries_addtional_info_updated} Countries additional info updated.\n')
        )

    def sync_conflicts(self, year):
        # Generate conflict snapshoot file
        self._generate_conflict_snapshot_file(year)
        conflict_old_ids = list(OldConflict.objects.using('idmc_platform').filter(year=year).values_list('id', flat=True))
        existing_conflicts_qs = NewConflict.objects.filter(old_id__in=conflict_old_ids, year=year)

        # Create conflict
        new_conflicts_ids = existing_conflicts_qs.values_list('old_id', flat=True)
        conflicts_to_add_ids = list(set(conflict_old_ids) - set(new_conflicts_ids))
        conflicts_added = NewConflict.objects.bulk_create(
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
                    old_id=old_conflict.id,
                ) for old_conflict in OldConflict.objects.using('idmc_platform').filter(
                    id__in=conflicts_to_add_ids,
                    year=year
                )
            ]
        )
        self.stdout.write(self.style.SUCCESS(f'{len(conflicts_added)} conflicts created.'))

        # Remove conflicts
        conflicts_to_remove_qs = existing_conflicts_qs.filter(
            ~Q(old_id__in=conflict_old_ids) & Q(year=year) & ~Q(old_id__in=conflicts_to_add_ids)
        )
        self.stdout.write(self.style.SUCCESS(f'{conflicts_to_remove_qs.count()} conflicts deleted.'))
        conflicts_to_remove_qs.delete()

        # Update conflicts
        conflicts_to_update_qs = existing_conflicts_qs.filter(old_id__in=conflict_old_ids, year=year)
        for new_conflict in conflicts_to_update_qs:
            old_conflict = OldConflict.objects.using('idmc_platform').get(id=new_conflict.old_id)
            new_conflict.country_id = self.get_country_id_from_iso3(old_conflict.iso3)
            new_conflict.year = old_conflict.year
            new_conflict.total_displacement = old_conflict.total_displacement
            new_conflict.total_displacement_source = old_conflict.total_displacement_source
            new_conflict.new_displacement = old_conflict.new_displacement
            new_conflict.new_displacement_source = old_conflict.new_displacement_source
            new_conflict.returns = old_conflict.returns
            new_conflict.returns_source = old_conflict.returns_source
            new_conflict.local_integration = old_conflict.local_integration
            new_conflict.local_integration_source = old_conflict.local_integration_source
            new_conflict.resettlement = old_conflict.resettlement
            new_conflict.resettlement_source = old_conflict.resettlement_source
            new_conflict.cross_border_flight = old_conflict.cross_border_flight
            new_conflict.cross_border_flight_source = old_conflict.cross_border_flight_source
            new_conflict.children_born_to_idps = old_conflict.children_born_to_idps
            new_conflict.children_born_to_idps_source = old_conflict.children_born_to_idps_source
            new_conflict.idp_deaths = old_conflict.idp_deaths
            new_conflict.idp_deaths_source = old_conflict.idp_deaths_source
            new_conflict.total_displacement_since = old_conflict.total_displacement_since
            new_conflict.new_displacement_since = old_conflict.new_displacement_since
            new_conflict.returns_since = old_conflict.returns_since
            new_conflict.resettlement_since = old_conflict.resettlement_since
            new_conflict.local_integration_since = old_conflict.local_integration_since
            new_conflict.cross_border_flight_since = old_conflict.cross_border_flight_since
            new_conflict.children_born_to_idps_since = old_conflict.children_born_to_idps_since
            new_conflict.idp_deaths_since = old_conflict.idp_deaths_since
            new_conflict.old_id = old_conflict.id
            new_conflict.save()
        self.stdout.write(self.style.SUCCESS(f'{conflicts_to_update_qs.count()} conflicts updated.\n'))

    def sync_disasters(self, year):
        # Generate disaster snaphot file
        self._generate_disaster_snapshot_file(year)

        disaster_old_ids = list(OldDisaster.objects.using('idmc_platform').filter(year=year).values_list('id', flat=True))
        existing_disasters_qs = NewDisaster.objects.filter(old_id__in=disaster_old_ids, year=year)

        # Create disasters
        new_disaster_ids = existing_disasters_qs.values_list('old_id', flat=True)
        disasters_to_add_ids = list(set(disaster_old_ids) - set(new_disaster_ids))
        disasters_added = NewDisaster.objects.bulk_create(
            [
                NewDisaster(
                    country_id=self.get_country_id_from_iso3(old_disaster.iso3),
                    year=old_disaster.year,
                    glide_number=old_disaster.glide_number,
                    event_name=self._capitalize_string(old_disaster.event_name),
                    location_text=old_disaster.location_text,
                    start_date=old_disaster.start_date,
                    start_date_accuracy=old_disaster.start_date_accuracy,
                    end_date=old_disaster.end_date,
                    end_date_accuracy=old_disaster.end_date_accuracy,
                    hazard_category=self._capitalize_string(old_disaster.hazard_category),
                    hazard_sub_category=self._capitalize_string(old_disaster.hazard_sub_category),
                    hazard_sub_type=self._capitalize_string(old_disaster.hazard_sub_type),
                    hazard_type=self._capitalize_string(old_disaster.hazard_type),
                    new_displacement=old_disaster.new_displacement,
                    new_displacement_source=old_disaster.new_displacement_source,
                    new_displacement_since=old_disaster.new_displacement_since,
                    old_id=old_disaster.id,
                ) for old_disaster in OldDisaster.objects.using('idmc_platform').filter(
                    id__in=disasters_to_add_ids, year=year
                )
            ]
        )
        self.stdout.write(self.style.SUCCESS(f'{len(disasters_added)} disasters created.'))

        # Remove disasters
        disasters_to_remove_qs = existing_disasters_qs.filter(~Q(old_id__in=new_disaster_ids, year=year))
        self.stdout.write(self.style.SUCCESS(f'{disasters_to_remove_qs.count()} disasters deleted.'))
        disasters_to_remove_qs.delete()

        # Update conflicts
        disaster_to_update_qs = existing_disasters_qs.filter(
            Q(old_id__in=disaster_old_ids) & Q(year=year) & ~Q(old_id__in=disasters_to_add_ids)
        )
        for new_disaster in disaster_to_update_qs:
            old_disaster = OldDisaster.objects.using('idmc_platform').get(id=new_disaster.old_id)
            new_disaster.country_id = self.get_country_id_from_iso3(old_disaster.iso3)
            new_disaster.year = old_disaster.year
            new_disaster.glide_number = old_disaster.glide_number
            new_disaster.event_name = self._capitalize_string(old_disaster.event_name)
            new_disaster.location_text = old_disaster.location_text
            new_disaster.start_date = old_disaster.start_date
            new_disaster.start_date_accuracy = old_disaster.start_date_accuracy
            new_disaster.end_date = old_disaster.end_date
            new_disaster.end_date_accuracy = old_disaster.end_date_accuracy
            new_disaster.hazard_category = self._capitalize_string(old_disaster.hazard_category)
            new_disaster.hazard_sub_category = self._capitalize_string(old_disaster.hazard_sub_category)
            new_disaster.hazard_sub_type = self._capitalize_string(old_disaster.hazard_sub_type)
            new_disaster.hazard_type = self._capitalize_string(old_disaster.hazard_type)
            new_disaster.new_displacement = old_disaster.new_displacement
            new_disaster.new_displacement_source = old_disaster.new_displacement_source
            new_disaster.new_displacement_since = old_disaster.new_displacement_since
            new_disaster.old_id = old_disaster.id
            new_disaster.save()
        self.stdout.write(self.style.SUCCESS(f'{disaster_to_update_qs.count()} disasters updated.\n'))

    def add_arguments(self, parser):
        parser.add_argument('year', type=int)

    def handle(self, *args, **options):
        year = options['year']
        if not year:
            self.stdout.write(self.style.ERROR('Please provide year'))
            return
        with open(os.path.join(
            settings.BASE_DIR, 'apps/old_gidd/management/commands/idmc_contacts.csv'), mode='r'
        ) as csv_file:
            contact_data = [
                {k: v for k, v in row.items()}
                for row in csv.DictReader(csv_file, skipinitialspace=True)
            ]

        with open(os.path.join(
            settings.BASE_DIR, 'apps/old_gidd/management/commands/figures_analysis.csv'), mode='r'
        ) as csv_file:
            figures_analysis_data = list(csv.reader(csv_file, skipinitialspace=True))

        self.sync_countries(contact_data, figures_analysis_data)
        self.sync_countries_addtional_info(year)
        self.sync_conflicts(year)
        self.sync_disasters(year)
