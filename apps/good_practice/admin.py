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
        'title', 'description', 'type', 'stage'
    ]
    inlines = [GalleryAdminInline, ]
    autocomplete_fields = ['countries', 'tags', 'focus_area', 'drivers_of_displacement']


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
