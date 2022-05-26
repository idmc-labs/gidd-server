from django.contrib import admin
from apps.common.models import StaticPage
from apps.common.forms import StaticPageForm


class StaticPageAdmin(admin.ModelAdmin):
    form = StaticPageForm
    search_fields = ['description']
    list_display = ['description', 'type']
    list_filter = ['type', ]


admin.site.register(StaticPage, StaticPageAdmin)
