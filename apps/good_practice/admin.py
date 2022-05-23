from django.contrib import admin
from apps.good_practice.models import (
    GoodPractice, Faq, MediaAndResourceLink
)
from apps.good_practice.form import (
    FaqForm, MediaAndResourceLinkForm, GoodPracticeForm
)


class FaqAdmin(admin.ModelAdmin):
    form = FaqForm
    search_fields = ['question']
    list_display = ['question', 'answer']


class MediaAndResourceLinkInline(admin.TabularInline):
    form = MediaAndResourceLinkForm
    autocomplete_fields = ['good_practice']
    model = MediaAndResourceLink
    extra = 0


class GoodPracticeAdmin(admin.ModelAdmin):
    form = GoodPracticeForm
    search_fields = ['name']
    list_display = [
        'title', 'description', 'country', 'type', 'drivers_of_dispalcement',
        'drivers_of_dispalcement', 'stage'
    ]
    autocomplete_fields = ['country', ]
    inlines = [MediaAndResourceLinkInline]


class MediaAndResourceLinkAdmin(admin.ModelAdmin):
    search_fields = ['link']
    list_display = ['id', 'link']
    autocomplete_fields = ['good_practice', ]


admin.site.register(Faq, FaqAdmin)
admin.site.register(GoodPractice, GoodPracticeAdmin)
admin.site.register(MediaAndResourceLink, MediaAndResourceLinkAdmin)
