from modeltranslation.translator import register, TranslationOptions

from .models import (
    Country,
)


@register(Country)
class CountryTO(TranslationOptions):
    fields = (
        'name',
    )
