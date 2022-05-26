from django.contrib import admin
from apps.good_practice.models import (
    GoodPractice, Faq,
)
from apps.good_practice.form import (
    FaqForm, GoodPracticeForm
)


class FaqAdmin(admin.ModelAdmin):
    form = FaqForm
    search_fields = ['question']
    list_display = ['question', 'answer']


class GoodPracticeAdmin(admin.ModelAdmin):
    form = GoodPracticeForm
    search_fields = ['name']
    list_display = [
        'title', 'description', 'country', 'type', 'drivers_of_dispalcement',
        'drivers_of_dispalcement', 'stage'
    ]
    autocomplete_fields = ['country', ]


admin.site.register(Faq, FaqAdmin)
admin.site.register(GoodPractice, GoodPracticeAdmin)
