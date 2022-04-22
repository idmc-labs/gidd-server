from django.db import models
from django.utils.translation import gettext_lazy as _


class Faq(models.Model):
    question = models.CharField(max_length=255, verbose_name=_('Question'))
    answer = models.TextField(blank=True, verbose_name=_('Answer'))

    class Meta:
        verbose_name = _('Frequently asked question')
        verbose_name_plural = _('Frequently asked questions')

    def __str__(self):
        return self.question


class GoodPractice(models.Model):
    class Type(models.TextChoices):
        # TODO: Change these enums
        ENUM_A = 'A', _('Enum A')
        ENUM_B = 'B', _('Enum B')

    class DriversOfDisplacementType(models.TextChoices):
        # TODO: Change these enums
        ENUM_A = 'A', _('Enum A')
        ENUM_B = 'B', _('Enum B')

    class TriggerType(models.TextChoices):
        # TODO: Change these enums
        ENUM_A = 'A', _('Enum A')
        ENUM_B = 'B', _('Enum B')

    class DisplacementImpactType(models.TextChoices):
        # TODO: Change these enums
        ENUM_A = 'A', _('Enum A')
        ENUM_B = 'B', _('Enum B')

    class InterventionPhaseType(models.TextChoices):
        # TODO: Change these enums
        ENUM_A = 'A', _('Enum A')
        ENUM_B = 'B', _('Enum B')

    class StageType(models.TextChoices):
        # TODO: Change these enums
        ENUM_A = 'A', _('Enum A')
        ENUM_B = 'B', _('Enum B')

    class TimeframeType(models.TextChoices):
        # TODO: Change these enums
        ENUM_A = 'A', _('Enum A')
        ENUM_B = 'B', _('Enum B')

    title = models.CharField(max_length=255, verbose_name=_('Title'))
    description = models.TextField(blank=True, verbose_name=_('Description'))
    country = models.ForeignKey(
        'country.Country', related_name='country_good_practice', on_delete=models.PROTECT,
        verbose_name=_('Country'), null=True, blank=True
    )
    type = models.CharField(
        max_length=255, verbose_name=_('Good practice type'), choices=Type.choices
    )
    drivers_of_dispalcement = models.CharField(
        max_length=255, verbose_name=_('Driver of displacement'), choices=DriversOfDisplacementType.choices
    )
    trigger = models.CharField(
        max_length=255, verbose_name=_('Trigger'), choices=TriggerType.choices
    )
    dispalcement_impact = models.CharField(
        max_length=255, verbose_name=_('Displacement impact'), choices=DisplacementImpactType.choices
    )
    intervention_phase = models.CharField(
        max_length=255, verbose_name=_('Intervention phase'), choices=InterventionPhaseType.choices
    )
    stage = models.CharField(
        max_length=255, verbose_name=_('Stage'), choices=StageType.choices
    )
    timeframe = models.CharField(
        max_length=255, verbose_name=_('Timeframe'), choices=TimeframeType.choices
    )

    class Meta:
        verbose_name = _('Good practice')
        verbose_name_plural = _('Good practices')

    def __str__(self):
        return self.title


class MediaAndResourceLink(models.Model):
    link = models.URLField(max_length=255, verbose_name=_('Media and resource link'))
    good_practice = models.ForeignKey(
        'good_practice.GoodPractice', related_name='country_essential_links', on_delete=models.PROTECT,
        verbose_name=_('Good practice'), null=True, blank=True
    )

    class Meta:
        verbose_name = _('Media and resource link')
        verbose_name_plural = _('Media and resource links')

    def __str__(self):
        return self.link
