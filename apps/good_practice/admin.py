from django.contrib import admin
from apps.good_practice.models import (
    GoodPractice, Faq, Gallery, Tag, FocusArea, DriversOfDisplacement
)
from apps.good_practice.form import (
    FaqForm, GoodPracticeForm, GalleryForm
)


class FaqAdmin(admin.ModelAdmin):
    form = FaqForm
    search_fields = ['question']
    list_display = ['question', 'answer']


class GalleryAdminInline(admin.TabularInline):
    autocomplete_fields = ['good_practice', ]
    form = GalleryForm
    model = Gallery
    extra = 0


class TagAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = [
        'name'
    ]


class GoodPracticeAdmin(admin.ModelAdmin):
    form = GoodPracticeForm
    search_fields = ['title']
    list_display = [
        'title', 'type', 'focus_areas', 'country_names', 'drivers_of_displacements', 'start_year', 'end_year'
    ]
    inlines = [GalleryAdminInline, ]
    autocomplete_fields = ['countries', 'tags', 'focus_area', 'drivers_of_displacement']

    def drivers_of_displacements(self, obj):
        return ", ".join([item.name for item in obj.drivers_of_displacement.all()])

    def focus_areas(self, obj):
        return ", ".join([item.name for item in obj.focus_area.all()])

    def country_names(self, obj):
        return ", ".join([item.name for item in obj.countries.all()])


class DriversOfDisplacementAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = [
        'name'
    ]


class FocusAreaAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = [
        'name'
    ]


admin.site.register(Faq, FaqAdmin)
admin.site.register(GoodPractice, GoodPracticeAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(DriversOfDisplacement, DriversOfDisplacementAdmin)
admin.site.register(FocusArea, FocusAreaAdmin)
