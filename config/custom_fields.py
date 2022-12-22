from django.conf import settings
from html_sanitizer import Sanitizer
from modeltranslation.utils import build_localized_fieldname


sanitizer = Sanitizer()


def clean_text_fields(obj, *fields):
    for field in fields:
        for lang, _ in settings.LANGUAGES:
            lang_field = build_localized_fieldname(field, lang)
            original_value = getattr(obj, lang_field, '')
            sanitized_value = sanitizer.sanitize(original_value or '')
            setattr(obj, lang_field, sanitized_value)
