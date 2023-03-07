from django.core.management.base import BaseCommand
import csv
import os
from django.utils import timezone
from django.conf import settings
from apps.country.models import Country
from apps.good_practice.models import GoodPractice, DriversOfDisplacement, FocusArea


class Command(BaseCommand):
    help = "Migrate good practices"

    def _clean_enum(self, text):
        return (
            text.lower()
            .replace(" ", "_")
            .replace(",", "")
            .replace("/", "_")
            .replace("-", "_")
        )

    def _get_type_enum(self, text):
        return GoodPractice.Type(self._clean_enum(text)).value

    def _get_countries_and_update_region(self, country_text, region_text):
        countries_name = [
            item.capitalize() for item in country_text.replace(" ", "").split(",")
        ]
        if "Elsalvador" in countries_name:
            countries_name = countries_name.remove("Elsalvador")
            if countries_name:
                countries_name.append(["El Salvador"])
            countries_name = ["El Salvador"]

        qs = Country.objects.filter(name__in=countries_name)
        if qs:
            qs.update(good_practice_region=self._clean_enum(region_text))
            return list(qs)
        else:
            print(country_text, "Country not found")
            return []

    def create_good_practice_data(self, good_practice_data):
        for good_practice_item in good_practice_data:
            good_practice = GoodPractice.objects.create(
                title=good_practice_item["Title"],
                start_year=good_practice_item["Year start"],
                end_year=good_practice_item["Year end"]
                if good_practice_item["Year end"]
                else None,
                type=self._get_type_enum(good_practice_item["Type of good practice"]),
                published_date=timezone.now(),
                is_published=True,
                stage=None,
            )
            good_practice.countries.add(
                *self._get_countries_and_update_region(
                    good_practice_item["Country"], good_practice_item["Region"]
                )
            )
            drivers_of_displacement_1 = (
                good_practice_item["Displacement drivers 1"].strip() or None
            )
            if drivers_of_displacement_1:
                (
                    drivers_of_displacement_obj_1,
                    created,
                ) = DriversOfDisplacement.objects.get_or_create(
                    name=drivers_of_displacement_1
                )
                good_practice.drivers_of_displacement.add(
                    drivers_of_displacement_obj_1.id
                )

            drivers_of_displacement_2 = (
                good_practice_item["Displacement drivers 2"].strip() or None
            )
            if drivers_of_displacement_2:
                (
                    drivers_of_displacement_obj_2,
                    created,
                ) = DriversOfDisplacement.objects.get_or_create(
                    name=drivers_of_displacement_2
                )
                good_practice.drivers_of_displacement.add(
                    drivers_of_displacement_obj_2.id
                )

            drivers_of_displacement_3 = (
                good_practice_item["Displacement drivers 3"].strip() or None
            )
            if drivers_of_displacement_3:
                (
                    drivers_of_displacement_obj_3,
                    created,
                ) = DriversOfDisplacement.objects.get_or_create(
                    name=drivers_of_displacement_3
                )
                good_practice.drivers_of_displacement.add(
                    drivers_of_displacement_obj_3.id
                )

            focus_area_1 = good_practice_item["Focus area 1"].strip() or None
            if focus_area_1:
                focus_area_obj_1, created = FocusArea.objects.get_or_create(
                    name=focus_area_1
                )
                good_practice.focus_area.add(focus_area_obj_1.id)

            focus_area_2 = good_practice_item["Focus area 2"].strip() or None
            if focus_area_2:
                focus_area_obj_2, created = FocusArea.objects.get_or_create(
                    name=focus_area_2
                )
                good_practice.focus_area.add(focus_area_obj_2.id)

            focus_area_3 = good_practice_item["Focus area 3"].strip() or None
            if focus_area_3:
                focus_area_obj_3, created = FocusArea.objects.get_or_create(
                    name=focus_area_3
                )
                good_practice.focus_area.add(focus_area_obj_3.id)

    def handle(self, *args, **options):
        with open(
            os.path.join(
                settings.BASE_DIR,
                "apps/good_practice/management/commands/good_practices.csv",
            ),
            mode="r",
        ) as csv_file:
            good_practice_data = [
                {k: v for k, v in row.items()}
                for row in csv.DictReader(csv_file, skipinitialspace=True)
            ]
        self.create_good_practice_data(good_practice_data)
