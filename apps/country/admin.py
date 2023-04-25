from django.contrib import admin
from reversion.admin import VersionAdmin
from modeltranslation.admin import TranslationAdmin
from apps.country.models import (
    Country,
    CountryAdditionalInfo,
    OverView,
    FigureAnalysis,
)
from apps.country.forms import (
    OverviewForm,
    CountryForm,
    FigureAnalysisForm,
)


class OverViewInline(admin.TabularInline):
    autocomplete_fields = ['country', ]
    model = OverView
    form = OverviewForm
    extra = 0


class FigureAnalysisInline(admin.TabularInline):
    autocomplete_fields = ['country', ]
    model = FigureAnalysis
    form = FigureAnalysisForm
    extra = 0


class CountryAdmin(VersionAdmin, TranslationAdmin):
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
    list_filter = [
        'idmc_continent',
        'idmc_region',
        'idmc_sub_region',
    ]
    inlines = [OverViewInline, FigureAnalysisInline, ]


class CountryAdditionalInfoAdmin(admin.ModelAdmin):
    list_display = [
        'year',
        'total_displacement',
        'total_displacement_since',
        'total_displacement_source',

    ]
    list_filter = ['year', ]
    search_fields = ['country__name']
    autocomplete_fields = ['country', ]


class OverViewAdmin(admin.ModelAdmin):
    search_fields = ['country__name']
    list_display = ['year', 'country', 'description', 'updated_at']
    autocomplete_fields = ['country', ]


admin.site.register(Country, CountryAdmin)
admin.site.register(CountryAdditionalInfo, CountryAdditionalInfoAdmin)
admin.site.register(OverView, OverViewAdmin)
