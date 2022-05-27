from django.core.management.base import BaseCommand
import csv
import os
from django.utils import timezone
from django.conf import settings
from apps.country.models import Country
from apps.good_practice.models import GoodPractice


class Command(BaseCommand):
    help = 'Migrate good practices'

    def _clean_enum(self, text):
        return text.lower().replace(" ", "_").replace(",", "").replace("/", "_")

    def _get_focus_area_enum(self, text):
        return GoodPractice.FocusArea(self._clean_enum(text)).value

    def _get_type_enum(self, text):
        return GoodPractice.Type(self._clean_enum(text)).value

    def _get_drivers_of_dispalcement_enum(self, text):
        return GoodPractice.DriversOfDisplacementType(self._clean_enum(text)).value

    def _get_countries_list(self, country_text):
        countries_name = [item.capitalize() for item in country_text.replace(" ", "").split(",")]
        if 'Elsalvador' in countries_name:
            countries_name = countries_name.remove('Elsalvador')
            if countries_name:
                countries_name.append(['El Salvador'])
            countries_name = ['El Salvador']

        qs = Country.objects.filter(name__in=countries_name)
        if qs:
            return list(qs)
        else:
            print(country_text, 'Country not found')
            return []

    def create_good_practice_data(self, good_practice_data):
        for good_practice_item in good_practice_data:
            good_practice = GoodPractice.objects.create(
                title=good_practice_item['Title'],
                start_year=good_practice_item['Year start'],
                end_year=good_practice_item['Year end'] if good_practice_item['Year end'] else None,
                focus_area=self._get_focus_area_enum(good_practice_item['Focus area 1']),
                type=self._get_type_enum(good_practice_item['Type of good practice']),
                drivers_of_displacement=self._get_drivers_of_dispalcement_enum(good_practice_item['Displacement drivers 1']),
                published_date=timezone.now(),
                is_published=True,
                stage=None
            )
            good_practice.countries.add(*self._get_countries_list(good_practice_item['Country']))

    def handle(self, *args, **options):
        with open(os.path.join(
            settings.BASE_DIR, 'apps/good_practice/management/commands/good_practices.csv'), mode='r'
        ) as csv_file:
            good_practice_data = [
                {k: v for k, v in row.items()}
                for row in csv.DictReader(csv_file, skipinitialspace=True)
            ]
        self.create_good_practice_data(good_practice_data)
