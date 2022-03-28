from django.contrib import admin
from apps.country.models import (
    Country, CountryAdditionalInfo
)


class CountryAdmin(admin.ModelAdmin):
    search_fields = ['name']
    autocomplete_fields = [
        'additional_info'
    ]


class CountryAdditionalInfoAdmin(admin.ModelAdmin):
    search_fields = ['country__name']


admin.site.register(Country, CountryAdmin)
admin.site.register(CountryAdditionalInfo, CountryAdditionalInfoAdmin)
