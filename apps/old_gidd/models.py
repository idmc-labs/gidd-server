# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Country(models.Model):
    iso3 = models.CharField(max_length=255, blank=True, null=True)
    iso2 = models.CharField(max_length=255, blank=True, null=True)
    idmc_names = models.CharField(max_length=255, blank=True, null=True)
    idmc_continent = models.CharField(max_length=255, blank=True, null=True)
    idmc_region = models.CharField(max_length=255, blank=True, null=True)
    idmc_sub_region = models.CharField(max_length=255, blank=True, null=True)
    wb_region = models.CharField(max_length=255, blank=True, null=True)
    un_population_division_names = models.CharField(max_length=255, blank=True, null=True)
    united_nations_region = models.CharField(max_length=255, blank=True, null=True)
    least_developed_countries = models.BooleanField(blank=True, null=True)
    small_island_developing_states = models.BooleanField(blank=True, null=True)
    idmc_go_2013 = models.BooleanField(blank=True, null=True)
    conflict_affected_since_1970 = models.BooleanField(blank=True, null=True)
    country_office_nrc = models.BooleanField(blank=True, null=True)
    country_office_iom = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Country'


class Conflict(models.Model):
    iso3 = models.TextField(blank=True, null=True)
    iso = models.TextField(blank=True, null=True)
    geo_name = models.TextField(blank=True, null=True)
    year = models.BigIntegerField(blank=True, null=True)
    total_displacement = models.BigIntegerField(blank=True, null=True)
    total_displacement_since = models.TextField(blank=True, null=True)
    total_displacement_source = models.TextField(blank=True, null=True)
    new_displacement = models.BigIntegerField(blank=True, null=True)
    new_displacement_since = models.TextField(blank=True, null=True)
    new_displacement_source = models.TextField(blank=True, null=True)
    returns = models.BigIntegerField(blank=True, null=True)
    returns_since = models.TextField(blank=True, null=True)
    returns_source = models.TextField(blank=True, null=True)
    local_integration = models.BigIntegerField(blank=True, null=True)
    local_integration_since = models.TextField(blank=True, null=True)
    local_integration_source = models.TextField(blank=True, null=True)
    resettlement = models.BigIntegerField(blank=True, null=True)
    resettlement_since = models.TextField(blank=True, null=True)
    resettlement_source = models.TextField(blank=True, null=True)
    cross_border_flight = models.BigIntegerField(blank=True, null=True)
    cross_border_flight_since = models.TextField(blank=True, null=True)
    cross_border_flight_source = models.TextField(blank=True, null=True)
    children_born_to_idps = models.BigIntegerField(blank=True, null=True)
    children_born_to_idps_since = models.TextField(blank=True, null=True)
    children_born_to_idps_source = models.TextField(blank=True, null=True)
    idp_deaths = models.BigIntegerField(blank=True, null=True)
    idp_deaths_since = models.TextField(blank=True, null=True)
    idp_deaths_source = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'conflict'


class ConflictBackupBeforeGrid2018(models.Model):
    iso3 = models.TextField(blank=True, null=True)
    iso = models.TextField(blank=True, null=True)
    geo_name = models.TextField(blank=True, null=True)
    year = models.BigIntegerField(blank=True, null=True)
    total_displacement = models.BigIntegerField(blank=True, null=True)
    total_displacement_since = models.TextField(blank=True, null=True)
    total_displacement_source = models.TextField(blank=True, null=True)
    new_displacement = models.BigIntegerField(blank=True, null=True)
    new_displacement_since = models.TextField(blank=True, null=True)
    new_displacement_source = models.TextField(blank=True, null=True)
    returns = models.BigIntegerField(blank=True, null=True)
    returns_since = models.TextField(blank=True, null=True)
    returns_source = models.TextField(blank=True, null=True)
    local_integration = models.BigIntegerField(blank=True, null=True)
    local_integration_since = models.TextField(blank=True, null=True)
    local_integration_source = models.TextField(blank=True, null=True)
    resettlement = models.BigIntegerField(blank=True, null=True)
    resettlement_since = models.TextField(blank=True, null=True)
    resettlement_source = models.TextField(blank=True, null=True)
    cross_border_flight = models.BigIntegerField(blank=True, null=True)
    cross_border_flight_since = models.TextField(blank=True, null=True)
    cross_border_flight_source = models.TextField(blank=True, null=True)
    children_born_to_idps = models.BigIntegerField(blank=True, null=True)
    children_born_to_idps_since = models.TextField(blank=True, null=True)
    children_born_to_idps_source = models.TextField(blank=True, null=True)
    idp_deaths = models.BigIntegerField(blank=True, null=True)
    idp_deaths_since = models.TextField(blank=True, null=True)
    idp_deaths_source = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'conflict_backup_before_grid_2018'


class ConflictTypology(models.Model):
    iso3 = models.TextField(blank=True, null=True)
    geo_name = models.TextField(blank=True, null=True)
    year = models.BigIntegerField(blank=True, null=True)
    conflict_typology = models.TextField(blank=True, null=True)
    new_displacement = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'conflict_typology'


class CountryDisasterInfo(models.Model):
    iso3 = models.CharField(max_length=3)
    year = models.BigIntegerField()
    total_displacement = models.BigIntegerField(blank=True, null=True)
    total_displacement_since = models.TextField(blank=True, null=True)
    total_displacement_source = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'country_disaster_info'
        unique_together = (('iso3', 'year'),)


class Disaster(models.Model):
    iso3 = models.TextField(blank=True, null=True)
    iso = models.TextField(blank=True, null=True)
    geo_name = models.TextField(blank=True, null=True)
    year = models.BigIntegerField(blank=True, null=True)
    glide_number = models.TextField(blank=True, null=True)
    event_name = models.TextField(blank=True, null=True)
    location_text = models.TextField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    start_date_accuracy = models.TextField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    end_date_accuracy = models.TextField(blank=True, null=True)
    hazard_category = models.TextField(blank=True, null=True)
    hazard_sub_category = models.TextField(blank=True, null=True)
    hazard_sub_type = models.TextField(blank=True, null=True)
    hazard_type = models.TextField(blank=True, null=True)
    new_displacement = models.BigIntegerField(blank=True, null=True)
    new_displacement_since = models.TextField(blank=True, null=True)
    new_displacement_source = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'disaster'


class DisasterBackupBeforeGrid2018(models.Model):
    iso3 = models.TextField(blank=True, null=True)
    iso = models.TextField(blank=True, null=True)
    geo_name = models.TextField(blank=True, null=True)
    year = models.BigIntegerField(blank=True, null=True)
    glide_number = models.TextField(blank=True, null=True)
    event_name = models.TextField(blank=True, null=True)
    location_text = models.TextField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    start_date_accuracy = models.TextField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    end_date_accuracy = models.TextField(blank=True, null=True)
    hazard_category = models.TextField(blank=True, null=True)
    hazard_sub_category = models.TextField(blank=True, null=True)
    hazard_sub_type = models.TextField(blank=True, null=True)
    hazard_type = models.TextField(blank=True, null=True)
    new_displacement = models.BigIntegerField(blank=True, null=True)
    new_displacement_since = models.TextField(blank=True, null=True)
    new_displacement_source = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'disaster_backup_before_grid_2018'


class EventsGrid2018(models.Model):
    iso3 = models.TextField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    subcategory = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    new_displacements = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'events_grid2018'


class EventsGrid2018Bkup20190514(models.Model):
    iso3 = models.TextField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    subcategory = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    new_displacements = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'events_grid2018_bkup20190514'


class GeoEntitiesBkup(models.Model):
    iso3 = models.CharField(primary_key=True, max_length=255)
    iso = models.CharField(max_length=255, blank=True, null=True)
    country_code = models.CharField(max_length=255, blank=True, null=True)
    idmc_short_name = models.CharField(max_length=255, blank=True, null=True)
    idmc_full_name = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    geographical_group = models.CharField(max_length=255, blank=True, null=True)
    region = models.TextField(blank=True, null=True)
    sub_region = models.TextField(blank=True, null=True)
    kampala_signed = models.BooleanField(blank=True, null=True)
    kampala_ratified = models.BooleanField(blank=True, null=True)
    sub_region_au = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'geo_entities_bkup'


class IncomeGroups(models.Model):
    iso3 = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    year = models.FloatField(blank=True, null=True)
    income_group = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'income_groups'


class LegacyNewDisplacementsByYear(models.Model):
    year = models.IntegerField()
    disaster_new_displacements = models.IntegerField(blank=True, null=True)
    conflict_new_displacements = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'legacy_new_displacements_by_year'


class LegacyStockDisplacementsVsRefugeesByYear(models.Model):
    year = models.IntegerField()
    stock_displacement = models.IntegerField(blank=True, null=True)
    refugees = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'legacy_stock_displacements_vs_refugees_by_year'


class Populations(models.Model):
    iso3 = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    loc_id_wpp = models.CharField(max_length=255, blank=True, null=True)
    name_wpp = models.CharField(max_length=255, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    figure = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'populations'


class Refugees(models.Model):
    iso3 = models.CharField(primary_key=True, max_length=3)
    year = models.BigIntegerField()
    figure = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'refugees__'
        unique_together = (('iso3', 'year'),)


class RefugeesUnhcrAndUnrwa(models.Model):
    year = models.IntegerField()
    figure = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'refugees_unhcr_and_unrwa'


class Sample(models.Model):
    sno = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    sname = models.CharField(max_length=10, blank=True, null=True)
    name = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sample'


class UnsdCountries(models.Model):
    global_code = models.IntegerField(db_column='Global Code', blank=True, null=True)
    global_name = models.CharField(db_column='Global Name', max_length=255, blank=True, null=True)
    region_code = models.IntegerField(db_column='Region Code', blank=True, null=True)
    region_name = models.CharField(db_column='Region Name', max_length=255, blank=True, null=True)
    sub_region_code = models.IntegerField(db_column='Sub-region Code', blank=True, null=True)
    sub_region_name = models.CharField(db_column='Sub-region Name', max_length=255, blank=True, null=True)
    intermediate_region_code = models.CharField(db_column='Intermediate Region Code', max_length=255, blank=True, null=True)
    intermediate_region_name = models.CharField(db_column='Intermediate Region Name', max_length=255, blank=True, null=True)
    country_or_area = models.CharField(db_column='Country or Area', max_length=255, blank=True, null=True)
    m49_code = models.IntegerField(db_column='M49 Code', blank=True, null=True)
    iso_alpha3_code = models.CharField(db_column='ISO-alpha3 Code', max_length=255, blank=True, null=True)
    least_developed_countries_ldc_field = models.CharField(
        db_column='Least Developed Countries (LDC)', max_length=255, blank=True, null=True
    )
    land_locked_developing_countries_lldc_field = models.CharField(
        db_column='Land Locked Developing Countries (LLDC)', max_length=255, blank=True, null=True
    )
    small_island_developing_states_sids_field = models.CharField(
        db_column='Small Island Developing States (SIDS)', max_length=255, blank=True, null=True
    )
    developed_developing_countries = models.CharField(
        db_column='Developed / Developing Countries', max_length=255, blank=True, null=True
    )

    class Meta:
        managed = False
        db_table = 'unsd_countries'


class UnverifiedPartialSolutions(models.Model):
    iso3 = models.TextField(primary_key=True)
    unverified_solutions = models.TextField(blank=True, null=True)
    unverified_solutions_year = models.TextField(blank=True, null=True)
    partial_solutions = models.TextField(blank=True, null=True)
    partial_solutions_year = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'unverified_partial_solutions'
