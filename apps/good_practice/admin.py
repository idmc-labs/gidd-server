from django.contrib import admin
from modeltranslation.admin import (
    TranslationAdmin,
    TranslationTabularInline
)
from apps.good_practice.models import (
    GoodPractice, Faq, Gallery, Tag, FocusArea, DriversOfDisplacement
)
from apps.good_practice.forms import (
    FaqForm, GoodPracticeForm, GalleryForm
)


@admin.register(Faq)
class FaqAdmin(TranslationAdmin):
    form = FaqForm
    search_fields = ['question']
    list_display = ['question', 'answer']


class GalleryAdminInline(TranslationTabularInline):
    autocomplete_fields = ['good_practice']
    form = GalleryForm
    model = Gallery
    extra = 0


@admin.register(Tag)
class TagAdmin(TranslationAdmin):
    search_fields = ['name']
    list_display = [
        'name'
    ]


@admin.register(GoodPractice)
class GoodPracticeAdmin(TranslationAdmin):
    form = GoodPracticeForm
    search_fields = ['title']
    list_display = [
        'title', 'type', 'focus_areas', 'country_names', 'drivers_of_displacements', 'start_year', 'end_year'
    ]
    inlines = [GalleryAdminInline]
    autocomplete_fields = ['countries', 'tags', 'focus_area', 'drivers_of_displacement']

    def drivers_of_displacements(self, obj):
        return ", ".join([item.name for item in obj.drivers_of_displacement.all()])

    def focus_areas(self, obj):
        return ", ".join([item.name for item in obj.focus_area.all()])

    def country_names(self, obj):
        return ", ".join([item.name for item in obj.countries.all()])


@admin.register(DriversOfDisplacement)
class DriversOfDisplacementAdmin(TranslationAdmin):
    search_fields = ['name']
    list_display = [
        'name'
    ]


@admin.register(FocusArea)
class FocusAreaAdmin(TranslationAdmin):
    search_fields = ['name']
    list_display = [
        'name'
    ]
