from django.db import models
from django.utils.translation import gettext_lazy as _
from utils import year_choices, current_year


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
        SOUTH_EAST_ASIA = 'south_east_asia', _('South-East Asia')
        SOUTHERN_EUROPE = 'southern_europe', _('Southern Europe')
        EAST_ASIA = 'east_asia', _('East Asia')
        NORTH_AMERICA = 'north_america', _('North America')
        SOUTH_ASIA = 'south_asia', _('South Asia')
        LATIN_AMERICA = 'latin_america', _('Latin America')
        WESTERN_AFRICA = 'western_africa', _('Western Africa')
        MICRONESIA = 'micronesia', _('Micronesia')
        HORN_OF_AFRICA = 'horn_of_africa', _('Horn of Africa')
        NORTH_WEST_AND_CENTRAL_EUROPE = 'north_west_and_central_europe', _('North, West and Central Europe')
        MELANESIA = 'melanesia', _('Melanesia')
        EASTERN_EUROPE = 'eastern_europe', _('Eastern Europe')
        AUSTRALIA_AND_NZ = 'australia_and_nz', _('Australia and NZ')
        CENTRAL_AFRICA = 'central_africa', _('Central Africa')
        POLYNESIA = 'polynesia', _('Polynesia')
        NORTHERN = 'northern_africa', _('Northern Africa')
        CENTRAL_ASIA = 'central_asia', _('Central Asia')
        WESTERN_ASIA = 'western_asia', _('Western Asia')
        SOUTHERN_AFRICA = 'southern_africa', _('Southern Africa')
        ASIA = 'asia', _('Asia')
        SOUTHERN_ASIA = 'southern_asia', _('Southren asia')
        EUROPE = 'europe', _('Europe')
        EUROPE_AND_SOUTHERN_ASIA = 'europe_and_central_asia', _('Europe and southern asia')
        ARFRICA = 'africa', _('Africa')
        MIDDLE_EAST_AND_NORTH_AFRICA = 'middle_east_and_north_africa', _('Middle east and north africa')
        OCEANIA = 'oceania', _('oceania')
        EAST_ASIA_AND_PACIFIC = 'east_asia_and_pacific', _('East asia and pacific')
        HIGH_INCOME_NON_OECD_MEMBER = 'high_income_non_oecd_member', _('high income non oecd member')
        SUB_SAHARAN_AFRICA = 'sub_saharan_africa', _('Sub saharan africa')
        MIDDLE_AFRICA = 'middle_africa', _('middle africa')
        AMERICAS = 'americas', _('Americas')
        HIGH_INCOME_OECD_MEMBER = 'high_income_oecd_member', _('high income oecd member')
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
    # Used in IDMC website
    background_image = models.FileField(upload_to='countries/', blank=True)
    title = models.CharField(max_length=255, verbose_name=_('Country title'), blank=True)
    description = models.TextField(blank=True, verbose_name=_('Country description'), null=True)
    essential_links = models.TextField(verbose_name=_('Essential links'), blank=True, null=True)
    contact_person_image = models.FileField(upload_to='contact_person/', blank=True)
    contact_person_description = models.TextField(
        verbose_name=_('Contact person description'), blank=True, null=True
    )

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

    class Meta:
        verbose_name = _('Country additional information')
        verbose_name_plural = _('Country additional informations')

    def __str__(self):
        return self.total_displacement_since if self.total_displacement_since else str(self.id)


class Conflict(models.Model):
    country = models.ForeignKey(
        'country.Country', related_name='country_conflict', on_delete=models.PROTECT,
        verbose_name=_('Country'), null=True, blank=True
    )
    year = models.BigIntegerField()
    total_displacement = models.BigIntegerField(blank=True, null=True)

    total_displacement_source = models.TextField(blank=True, null=True)
    new_displacement = models.BigIntegerField(blank=True, null=True)
    new_displacement_source = models.TextField(blank=True, null=True)
    returns = models.BigIntegerField(blank=True, null=True)
    returns_source = models.TextField(blank=True, null=True)
    local_integration = models.BigIntegerField(blank=True, null=True)
    local_integration_source = models.TextField(blank=True, null=True)
    resettlement = models.BigIntegerField(blank=True, null=True)
    resettlement_source = models.TextField(blank=True, null=True)
    cross_border_flight = models.BigIntegerField(blank=True, null=True)
    cross_border_flight_source = models.TextField(blank=True, null=True)
    children_born_to_idps = models.BigIntegerField(blank=True, null=True)
    children_born_to_idps_source = models.TextField(blank=True, null=True)
    idp_deaths = models.BigIntegerField(blank=True, null=True)
    idp_deaths_source = models.TextField(blank=True, null=True)

    # TODO: Should we change thses fields to DateField?
    total_displacement_since = models.TextField(blank=True, null=True)
    new_displacement_since = models.TextField(blank=True, null=True)
    returns_since = models.TextField(blank=True, null=True)
    resettlement_since = models.TextField(blank=True, null=True)
    local_integration_since = models.TextField(blank=True, null=True)
    cross_border_flight_since = models.TextField(blank=True, null=True)
    children_born_to_idps_since = models.TextField(blank=True, null=True)
    idp_deaths_since = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = _('Conflict')
        verbose_name_plural = _('Conflicts')

    def __str__(self):
        return str(self.year)


class Disaster(models.Model):
    country = models.ForeignKey(
        'country.Country', related_name='country_disaster', on_delete=models.PROTECT,
        verbose_name=_('Country'), null=True, blank=True
    )
    year = models.BigIntegerField()
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
    new_displacement_source = models.TextField(blank=True, null=True)
    new_displacement_since = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = _('Disaster')
        verbose_name_plural = _('Disasters')

    def __str__(self):
        return str(self.year)
