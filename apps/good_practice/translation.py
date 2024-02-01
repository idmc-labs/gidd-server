from modeltranslation.translator import register, TranslationOptions

from .models import (
    Faq,
    Tag,
    DriversOfDisplacement,
    FocusArea,
    GoodPractice,
    Gallery,
    SuccessFactor,
)


@register(Faq)
class FaqTO(TranslationOptions):
    fields = (
        "question",
        "answer",
    )


@register(Tag)
class TagTO(TranslationOptions):
    fields = ("name",)


@register(DriversOfDisplacement)
class DriversOfDisplacementTO(TranslationOptions):
    fields = ("name",)


@register(FocusArea)
class FocusAreaTO(TranslationOptions):
    fields = ("name",)


@register(GoodPractice)
class GoodPracticeTO(TranslationOptions):
    fields = (
        "title",
        "description",
        "media_and_resource_links",
        "implementing_entity",
    )


@register(Gallery)
class GalleryTO(TranslationOptions):
    fields = ("caption",)


@register(SuccessFactor)
class SuccessFactorTO(TranslationOptions):
    fields = ("name",)
