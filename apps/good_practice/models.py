from django.db import models
from django.utils.translation import gettext_lazy as _


class Faq(models.Model):
    question = models.CharField(max_length=255, verbose_name=_('Question'))
    answer = models.TextField(blank=True, verbose_name=_('Answer'))
    is_published = models.BooleanField(
        default=False, verbose_name=_('Is published?')
    )

    class Meta:
        verbose_name = _('Frequently asked question')
        verbose_name_plural = _('Frequently asked questions')

    def __str__(self):
        return self.question


class GoodPractice(models.Model):
    class Type(models.TextChoices):
        POLICIES_STRATEGIES_AND_LEAGAL_FRAMEWORKS = (
            'policies_strategies_and_legal_frameworks',
            _('Policies, strategies and legal frameworks')
        )
        GOVERNANCE_CAPACITY_AND_INSTITUTIONAL_SET_UP = (
            'governance_capacity_and_institutional_set_up',
            _('Governance capacity and institutional set-up')
        )
        DISPLACEMENT_MONITORING_DATA_COLLECTION_ANALYSIS_AND_SYSTEMS = (
            'displacement_monitoring_data_collection_analysis_and_systems',
            _('Displacement monitoring (data collection, analysis and systems)')
        )
        RISK_REDUCTION_AND_PREVENTION = (
            'risk_reduction_and_prevention',
            _('Risk Reduction and Prevention (DRR, CCA and peacebuilding)')
        )
        PROTECTION_AND_ASSISTANCE_AND_DURABLE_SOLUTIONS = (
            'protection_and_assistance_and_durable_solutions',
            _('Protection and assistance, and durable solutions')
        )

    class DriversOfDisplacementType(models.TextChoices):
        SLOW_ONSET_DISASTERS = 'slow_onset_disasters', _('Slow onset disasters')
        SUDDEN_ONSET_DISASTERS = 'sudden_onset_disasters', _('Sudden onset disasters')
        CONFLICT_AND_VIOLENCE = 'conflict_and_violence', _('Conflict and violence')
        DEVELOPMENT_AND_URBANISATION = 'development_and_urbanisation', _('Development and urbanisation')

    class StageType(models.TextChoices):
        PROMISING = 'promising', _('Promising')
        ADVANCED = 'advanced', _('Advanced')
        SUCCESSFUL = 'successful', _('Successful')

    class FocusArea(models.TextChoices):
        HEALTH = 'health', _('Health')
        EDUCATION = 'education', _('Education')
        LIVELIHOODS_AND_EMPLOYMENT = 'livelihoods_and_employment', _('Livelihoods and employment')
        HOUSING_LAND_AND_PROPERTY = 'housing_land_and_property', _('Housing, land and property')
        FOOD_AND_WATER_INSECURITY = 'food_and_water_insecurity', _('Food and water insecurity')
        SOCIAL_PROTECTION_AND_ASSISTANCE = 'social_protection_and_assistance', _('Social protection and assistance')
        SAFETY_AND_SECUTIRY = 'safety_and_security', _('Safety and social security')
        CIVIC_AND_SOCIAL_RIGHTS = 'civic_and_social_rights', _('Civic and social rights')
        ENVIRONMENT = 'environment', _('Environment'),
        GENDER = 'gender', _('Gender')
        DISABILITY = 'disability', _('Disability')
        CHILDREN_AND_YOUTH = 'children_and_youth', _('Children and youth')

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
    stage = models.CharField(
        max_length=255, verbose_name=_('Stage'), choices=StageType.choices
    )
    focus_area = models.CharField(
        max_length=255, verbose_name=_('Stage'), choices=FocusArea.choices
    )
    is_published = models.BooleanField(
        default=False, verbose_name=_('Is published?')
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
    is_published = models.BooleanField(
        default=False, verbose_name=_('Is published?')
    )

    class Meta:
        verbose_name = _('Media and resource link')
        verbose_name_plural = _('Media and resource links')

    def __str__(self):
        return self.link
