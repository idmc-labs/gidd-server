from django.db import models
from django.utils.translation import gettext_lazy as _


class StaticPage(models.Model):
    class StaticPageType(models.TextChoices):
        GOOD_PRACTICE_LISTING_PAGE = 'good_practice_listing_page', _('Good practice listing page')
        SUBMIT_GOOD_PRACTICE = 'submit_good_practice', _('Submit good practice')
        GOOD_PRACTICE_CONTACT_INFORMATION = 'good_practice_contact_information', _('Good practice contact information')

    type = models.CharField(
        max_length=255, verbose_name=_('Static page type'), choices=StaticPageType.choices
    )
    description = models.TextField(blank=True, verbose_name=_('Caption'), null=True)

    class Meta:
        verbose_name = _('Static page')
        verbose_name_plural = _('Static pages')

    def __str__(self):
        return self.type
