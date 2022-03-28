from django.db import models
from django.utils.translation import gettext_lazy as _


class Country(models.Model):

    class Continent(models.TextChoices):
        EUROPE = 'europe', _('Europe')
        OCEANIA = 'oceania', _('Oceania')
        AMERICAS = 'americas', _('Americas')
        AFRICA = 'africa', _('Africa')
        ASIA = 'asia', _('Asia')
        ANTARTICA = 'Antarctica', _('Antarctica')

    class Region(models.TextChoices):
        CARIBBEAN = 'caribbean', _('Caribbean')
        SOUTH_EAST_ASIA = 'south-east-asia', _('South-East Asia')
        SOUTHERN_EUROPE = 'southern_europe', _('Southern Europe')
        EAST_ASIA = 'east_asia', _('East Asia')
        NORTH_AMERICA = 'north_america', _('North America')
        SOUTH_ASIA = 'south_asia', _('South Asia')
        LATIN_AMERICA = 'latin_america', _('Latin America')
        WESTERN_AFRICA = 'western_africa', _('Western Africa')
        MICRONESIA = 'micronesia', _('Micronesia')
        HORN_OR_AFRICA = 'horn_of_africa', _('Horn of Africa')
        NORTH_WEST_AND_CENTRAL_EUROPE = 'north_west_and_central_europe', _('North, West and Central Europe')
        MELANESIA = 'melanesia', _('Melanesia')
        EASTERN_EUROPE = 'eastern_europe', _('Eastern Europe')
        AUSTRALIA_AND_NZ = 'australia_and_nz', _('Australia and NZ')
        CENTRAL_AFRICA = 'central_africa', _('Central Africa')
        POLYNESIA = 'polynesia', _('Polynesia')
        NORTHERN = 'northern_africa', _('Northern Africa')
        CENTRAL_ASIA = 'central_asia', _('Central Asia')
        WESTERN_ASIA = 'western_asia', _('Western Asia')
        SOUTHERN_AFRICA = 'southern-africa', _('Southern Africa')

    class SubRegion(models.TextChoices):
        CARIBBEAN = 'south-caucasus', _('South Caucasus')
        LATIN_AMERICA = 'latin-america', _('Latin America')
        MIDDLE_EAST = 'middle-east', _('Middle East')

    name = models.CharField(max_length=255, verbose_name=_('Name'))
    iso3 = models.CharField(max_length=10, verbose_name=_('Iso3'))
    iso2 = models.CharField(max_length=255, verbose_name=_('Iso2'))
    idmc_names = models.CharField(null=True, blank=True, max_length=255, verbose_name=_('Idmc names'))
    idmc_continent = models.CharField(
        choices=Continent.choices, max_length=100, verbose_name=_('Idmc continent'),
        null=True, blank=True
    )
    idmc_region = models.CharField(
        choices=Region.choices, max_length=100, verbose_name=_('Idmc region'),
        null=True, blank=True
    )
    idmc_sub_region = models.CharField(
        choices=SubRegion.choices, max_length=100, verbose_name=_('Idmc sub region'),
        null=True, blank=True
    )
    wb_region = models.CharField(
        choices=Region.choices, max_length=100, verbose_name=_('Wb region'),
        null=True, blank=True
    )
    un_population_division_names = models.CharField(
        null=True, blank=True, max_length=255, verbose_name=_('Unpopulation division name')
    )
    united_nations_region = models.CharField(
        choices=Region.choices, max_length=100, verbose_name=_('United nations region'),
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
    additional_info = models.OneToOneField(
        'country.CountryAdditionalInfo',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name=_('Additional info')
    )

    class Meta:
        verbose_name = _('Country')
        verbose_name_plural = _('Countries')

    def __str__(self):
        return self.name


class CountryAdditionalInfo(models.Model):
    total_displacement = models.BigIntegerField(blank=True, null=True)
    total_displacement_since = models.TextField(blank=True, null=True)
    total_displacement_source = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = _('CountryAdditional Info')
        verbose_name_plural = _('CountryAdditional Infos')

    def __str__(self):
        return self.total_displacement_since + self.total_displacement_source
