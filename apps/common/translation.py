from modeltranslation.translator import register, TranslationOptions

from .models import (
    StaticPage
)


@register(StaticPage)
class StaticPageTO(TranslationOptions):
    fields = (
        'description',
    )
