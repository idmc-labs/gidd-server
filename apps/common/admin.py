from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from apps.common.models import StaticPage
from apps.common.forms import StaticPageForm


@admin.register(StaticPage)
class StaticPageAdmin(TranslationAdmin):
    form = StaticPageForm
    search_fields = ['description']
    list_display = ['description', 'type']
    list_filter = ['type']
