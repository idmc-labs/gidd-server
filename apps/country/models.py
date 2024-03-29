from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.utils.translation import gettext_lazy as _
from utils import year_choices, current_year
import config.custom_fields  # noqa F401 NOTE this is added to sanitize the text fields through out the project


class Country(models.Model):

    class Continent(models.TextChoices):
        EUROPE = 'europe', _('Europe')
        OCEANIA = 'oceania', _('Oceania')
        AMERICAS = 'americas', _('Americas')
        AFRICA = 'africa', _('Africa')
        ASIA = 'asia', _('Asia')
        ANTARTICA = 'Antarctica', _('Antarctica')

    class IdmcRegion(models.TextChoices):
        AUSTRALIA_AND_NZ = 'australia_and_nz', _('Australia and NZ')
        CARIBBEAN = 'caribbean', _('Caribbean')
        CENTRAL_AFRICA = 'central_africa', _('Central Africa')
        CENTRAL_ASIA = 'central_asia', _('Central Asia')
        EAST_ASIA = 'east_asia', _('East Asia')
        EASTERN_EUROPE = 'eastern_europe', _('Eastern Europe')
        HORN_OF_AFRICA = 'horn_of_africa', _('Horn of Africa')
        LATIN_AMERICA = 'latin_america', _('Latin America')
        MELANESIA = 'melanesia', _('Melanesia')
        MICRONESIA = 'micronesia', _('Micronesia')
        NORTH_AMERICA = 'north_america', _('North America')
        NORTHERN_AFRICA = 'northern_africa', _('Northern Africa')
        NORTH_WEST_AND_CENTRAL_EUROPE = 'north_west_and_central_europe', _('North, West and Central Europe')
        POLYNESIA = 'polynesia', _('Polynesia')
        SOUTH_ASIA = 'south_asia', _('South Asia')
        SOUTH_EAST_ASIA = 'south_east_asia', _('South-East Asia')
        SOUTHERN_AFRICA = 'southern_africa', _('Southern Africa')
        SOUTHERN_EUROPE = 'southern_europe', _('Southern Europe')
        WESTERN_AFRICA = 'western_africa', _('Western Africa')
        WESTERN_ASIA = 'western_asia', _('Western Asia')

    class WbRegion(models.TextChoices):
        EAST_ASIA_AND_PACIFIC = 'east_asia_and_pacific', _('East asia and pacific')
        EUROPE_AND_CENTRAL_ASIA = 'europe_and_central_asia', _('Europe and Central Asia')
        HIGH_INCOME_OECD_MEMBER = 'high_income_oecd_member', _('high income oecd member')
        HIGH_INCOME_NON_OECD_MEMBER = 'high_income_non_oecd_member', _('high income non oecd member')
        LATIN_AMERICA_AND_THE_CARIBBEAN = 'latin_america_and_the_caribbean', _('Latin America and the Caribbean')
        MIDDLE_EAST_AND_NORTH_AFRICA = 'middle_east_and_north_africa', _('Middle east and north africa')
        SOUTH_ASIA = 'south_asia', _('South Asia')
        SUB_SAHARAN_AFRICA = 'sub_saharan_africa', _('Sub-Saharan Africa')

    class UnitedNationsRegion(models.TextChoices):
        ASIA = 'asia', _('Asia')
        SOUTHERN_ASIA = 'southern_asia', _('Southren asia')
        EUROPE = 'europe', _('Europe')
        EUROPE_AND_SOUTHERN_ASIA = 'europe_and_central_asia', _('Europe and southern asia')
        ARFRICA = 'africa', _('Africa')
        OCEANIA = 'oceania', _('oceania')
        SUB_SAHARAN_AFRICA = 'sub_saharan_africa', _('Sub saharan africa')
        MIDDLE_AFRICA = 'middle_africa', _('middle africa')
        AMERICAS = 'americas', _('Americas')
        LATIN_AMERICA_AND__THE_CARIBBEAN = 'latin_america_and_the_caribbean', _('latin america and the caribbean')
        SOUTH_AMERICA = 'south_america', _('South america')
        AUSTRALIA_AND_NEW_ZEALAND = 'australia_and_new_zealand', _('Australia and new zealand')
        WESTERN_EUROPE = 'western_europe', _('Western europe')
        CENTRAL_AMERICA = 'central_america', _('Central america')
        NORTHEN_AMERICA = 'northern_america', _('northern america')
        SOUTH_EASTERN_ASIA = 'south_eastern_asia', _('South eastern asia')
        EASTERN_AFRICA = 'eastern_africa', _('Eastern africa')
        EASTERN_ASIA = 'eastern_asia', _('Eastern asia')
        NORTHERN_EUROPE = 'northern_europe', _('Northern europe')

    class SubRegion(models.TextChoices):
        CARIBBEAN = 'caribbean', _('Caribbean')
        LATIN_AMERICA = 'latin_america', _('Latin America')
        MIDDLE_EAST = 'middle_east', _('Middle East')
        SOUTH_CAUCASUS = 'south_caucasus', _('South caucasus')

    class GoodPracticeRegion(models.TextChoices):
        THE_AMERICAS = 'the_americas', _('The Americas')
        SUB_SAHARAN_AFRICA = 'sub_saharan_africa', _('Sub-Saharan Africa')
        SOUTH_ASIA = 'south_asia', _('South Asia')
        MIDDLE_EAST_AND_NORTH_AFRICA = 'middle_east_and_north_africa', _('Middle East and North Africa')
        EAST_ASIA_AND_THE_PACIFIC = 'east_asia_and_the_pacific', _('East Asia and the Pacific')
        EUROPE_AND_CENTRAL_ASIA = 'europe_and_central_asia', _('Europe and Central Asia')

    id: int
    name = models.CharField(max_length=255, verbose_name=_('Name'))
    iso3 = models.CharField(max_length=10, verbose_name=_('Iso3'))
    iso2 = models.CharField(max_length=255, verbose_name=_('Iso2'))
    idmc_names = models.CharField(null=True, blank=True, max_length=255, verbose_name=_('Idmc names'))
    idmc_continent = models.CharField(
        choices=Continent.choices, max_length=100, verbose_name=_('Idmc continent'),
        null=True, blank=True
    )
    idmc_region = models.CharField(
        choices=IdmcRegion.choices, max_length=100, verbose_name=_('Idmc region'),
        null=True, blank=True
    )
    idmc_sub_region = models.CharField(
        choices=SubRegion.choices, max_length=100, verbose_name=_('Idmc sub region'),
        null=True, blank=True
    )
    wb_region = models.CharField(
        choices=WbRegion.choices, max_length=100, verbose_name=_('Wb region'),
        null=True, blank=True
    )
    un_population_division_names = models.CharField(
        null=True, blank=True, max_length=255, verbose_name=_('Unpopulation division name')
    )
    united_nations_region = models.CharField(
        choices=UnitedNationsRegion.choices, max_length=100, verbose_name=_('United nations region'),
        null=True, blank=True
    )
    good_practice_region = models.CharField(
        choices=GoodPracticeRegion.choices, max_length=100, verbose_name=_('Good practice region'),
        null=True, blank=True
    )
    is_least_developed_country = models.BooleanField(
        default=False, verbose_name=_('Is least developed country?')
    )
    is_small_island_developing_state = models.BooleanField(
        default=False, verbose_name=_('Is small island developing state?')
    )
    is_idmc_go_2013 = models.BooleanField(
        default=False, verbose_name=_('Is idmc go 2013?')
    )
    is_conflict_affected_since_1970 = models.BooleanField(
        default=False, verbose_name=_('Is conflict affected since 1970?')
    )
    is_country_office_nrc = models.BooleanField(
        default=False, verbose_name=_('Is country office nrc?')
    )
    is_country_office_iom = models.BooleanField(
        default=False, verbose_name=_('Is country office iom?')
    )
    bounding_box = ArrayField(
        verbose_name=_('Bounding Box'),
        base_field=models.FloatField(blank=False), null=True
    )
    center_point = ArrayField(
        verbose_name=_('Center point'),
        base_field=models.FloatField(blank=False), null=True
    )
    # Used in IDMC website
    background_image = models.FileField(upload_to='countries/', blank=True)
    title = models.CharField(max_length=255, verbose_name=_('Country title'), blank=True)
    description = models.TextField(blank=True, verbose_name=_('Country description'), null=True)
    essential_links = models.TextField(verbose_name=_('Essential links'), blank=True, null=True)
    contact_person_image = models.FileField(upload_to='contact_person/', blank=True)
    contact_person_description = models.TextField(
        verbose_name=_('Contact person description'), blank=True, null=True
    )
    internal_displacement_description = models.TextField(
        blank=True, verbose_name=_('Internal displacement description'), null=True
    )
    displacement_data_description = models.TextField(
        blank=True, verbose_name=_('Displacement data description'), null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('Country')
        verbose_name_plural = _('Countries')

    def __str__(self):
        return self.name

    @property
    def country_additional_info(self):
        return self.country_additonal_info


class OverView(models.Model):
    country = models.ForeignKey(
        'country.Country', related_name='country_overviews', on_delete=models.PROTECT,
        verbose_name=_('Country'), null=True, blank=True
    )
    description = models.TextField(blank=True, verbose_name=_('Country description'), null=True)
    year = models.IntegerField(_('year'), choices=year_choices(), default=current_year())
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Updated at'))
    is_published = models.BooleanField(
        default=False, verbose_name=_('Is published?')
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('Country overview')
        verbose_name_plural = _('Country overviews')

    def __str__(self):
        return self.description if self.description else str(self.updated_at)


class CountryAdditionalInfo(models.Model):
    country = models.ForeignKey(
        'country.Country', related_name='country_additonal_info', on_delete=models.PROTECT,
        verbose_name=_('Country'), null=True, blank=True
    )
    year = models.BigIntegerField(blank=True, null=True)
    total_displacement = models.BigIntegerField(blank=True, null=True)
    total_displacement_since = models.TextField(blank=True, null=True)
    total_displacement_source = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('Country additional information')
        verbose_name_plural = _('Country additional informations')

    def __str__(self):
        return self.total_displacement_since if self.total_displacement_since else str(self.id)
