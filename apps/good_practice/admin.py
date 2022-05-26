from django.contrib import admin
from apps.good_practice.models import (
    GoodPractice, Faq, Gallery
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


class GoodPracticeAdmin(admin.ModelAdmin):
    form = GoodPracticeForm
    search_fields = ['name']
    list_display = [
        'title', 'description', 'type', 'drivers_of_dispalcement',
        'drivers_of_dispalcement', 'stage'
    ]
    inlines = [GalleryAdminInline, ]
    autocomplete_fields = ['countries', ]


admin.site.register(Faq, FaqAdmin)
admin.site.register(GoodPractice, GoodPracticeAdmin)
