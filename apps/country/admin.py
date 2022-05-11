from django.contrib import admin
from reversion.admin import VersionAdmin
from apps.country.models import (
    Country, CountryAdditionalInfo,
    Conflict, Disaster, OverView
)
from apps.country.form import (
    OverviewForm, CountryForm
)


class OverViewInline(admin.TabularInline):
    autocomplete_fields = ['country', ]
    model = OverView
    form = OverviewForm
    extra = 0


class CountryAdmin(VersionAdmin):
    search_fields = ['name']
    list_display = [
        'iso3',
        'iso2',
        'name',
        'idmc_names',
        'idmc_continent',
        'idmc_region',
        'idmc_sub_region',
        'wb_region',
        'un_population_division_names',
        'united_nations_region',
        'is_least_developed_country',
        'is_small_island_developing_state',
        'is_idmc_go_2013',
        'is_conflict_affected_since_1970',
        'is_country_office_nrc',
        'is_country_office_iom',
    ]
    form = CountryForm
    inlines = [OverViewInline, ]


class CountryAdditionalInfoAdmin(admin.ModelAdmin):
    list_display = [
        'year',
        'total_displacement',
        'total_displacement_since',
        'total_displacement_source',

    ]
    search_fields = ['country__name']
    autocomplete_fields = ['country', ]


class ConflictAdmin(admin.ModelAdmin):
    search_fields = ['country__name']
    list_display = [
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

    ]
    autocomplete_fields = ['country', ]


class DisasterAdmin(admin.ModelAdmin):
    search_fields = ['country__name']
    list_display = [
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
    ]
    autocomplete_fields = ['country', ]


class OverViewAdmin(admin.ModelAdmin):
    search_fields = ['country__name']
    list_display = ['year', 'country', 'description', 'updated_at']
    autocomplete_fields = ['country', ]


admin.site.register(Country, CountryAdmin)
admin.site.register(CountryAdditionalInfo, CountryAdditionalInfoAdmin)
admin.site.register(Conflict, ConflictAdmin)
admin.site.register(Disaster, DisasterAdmin)
admin.site.register(OverView, OverViewAdmin)
