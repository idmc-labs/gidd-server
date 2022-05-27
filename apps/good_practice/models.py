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
        RISK_REDUCTION_AND_PREVENTION = (
            'risk_reduction_and_prevention',
            _('Risk Reduction and Prevention (DRR, CCA and peacebuilding)')
        )
        PROTECTION_AND_ASSISTANCE_AND_DURABLE_SOLUTIONS = (
            'protection_and_assistance_and_durable_solutions',
            _('Protection and assistance, and durable solutions')
        )
        STRENGTHENING_POLICY_AND_LEGAL_FRAMEWORKS = (
            'strengthening_policy_and_legal_frameworks',
            _('Strengthening policy and legal frameworks')
        )
        INTERVENTIONS = 'interventions', _('Interventions')
        POLICIES = 'policies', _('Policies')

    class DriversOfDisplacementType(models.TextChoices):
        INCREASING_TEMPERATURES_DROUGHT_AND_DESERTIFICATION = (
            'increasing_temperatures_drought_and_desertification', _('Increasing temperatures, drought, and desertification')
        )
        LAND_FOREST_DEGRADATION_AND_LOSS_OF_BIODIVERSITY = (
            'land_forest_degradation_and_loss_of_biodiversity', _('Land/forest degradation and loss of biodiversity')
        )
        SEA_LEVEL_RISE_SALINIZATION_AND_OCEAN_ACIDIFICATION = (
            'sea_level_rise_salinization_and_ocean_acidification', _('Sea level rise, salinization, and ocean acidification')
        )
        GLACIAL_MELT = 'glacial_melt', _('Glacial melt')
        FLOODS = 'floods', _('Floods')
        LANDSLIDES = 'landslides', _('Landslides')

    class StageType(models.TextChoices):
        PROMISING = 'promising', _('Promising')
        ADVANCED = 'advanced', _('Advanced')
        SUCCESSFUL = 'successful', _('Successful')

    class FocusArea(models.TextChoices):
        LIVELIHOODS_AND_EMPLOYMENT = 'livelihoods_and_employment', _('Livelihoods and employment')
        SAFETY_AND_SECUTIRY = 'safety_and_security', _('Safety and social security')
        HEALTH = 'health', _('Health')
        EDUCATION = 'education', _('Education')
        HOUSING_LAND_AND_PROPERTY = 'housing_land_and_property', _('Housing, land and property')
        ENVIRONMENT = 'environment', _('Environment'),
        FOOD_AND_WATER_INSECURITY = 'food_and_water_insecurity', _('Food and water insecurity')
        SOCIAL_PROTECTION_AND_ASSISTANCE = 'social_protection_and_assistance', _('Social protection and assistance')

    title = models.CharField(max_length=255, verbose_name=_('Title'))
    description = models.TextField(blank=True, verbose_name=_('Description'), null=True)
    media_and_resource_links = models.TextField(blank=True, verbose_name=_('Media and resource links'), null=True)
    countries = models.ManyToManyField(
        'country.Country', related_name='country_good_practice', verbose_name=_('Countries')
    )
    type = models.CharField(
        max_length=255, verbose_name=_('Good practice type'), choices=Type.choices
    )
    drivers_of_displacement = models.CharField(
        max_length=255, verbose_name=_('Driver of displacement'), choices=DriversOfDisplacementType.choices
    )
    stage = models.CharField(
        max_length=255, verbose_name=_('Stage'), choices=StageType.choices, null=True, blank=True
    )
    focus_area = models.CharField(
        max_length=255, verbose_name=_('Focus area'), choices=FocusArea.choices
    )
    published_date = models.DateTimeField(blank=True)
    image = models.FileField(upload_to='good_practice/', blank=True, verbose_name=_('Good practices'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created at'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Updated at'))
    good_practice_form_url = models.URLField(max_length=255, verbose_name=_('Good practice form URL'))
    is_published = models.BooleanField(
        default=False, verbose_name=_('Is published?')
    )
    start_year = models.BigIntegerField(verbose_name=_('Start year'))
    end_year = models.BigIntegerField(blank=True, null=True, verbose_name=_('End year'))
    page_viewed_count = models.BigIntegerField(default=0, verbose_name=_('Total page viewed count'))

    class Meta:
        verbose_name = _('Good practice')
        verbose_name_plural = _('Good practices')

    def __str__(self):
        return self.title


class Gallery(models.Model):
    youtube_video_url = models.URLField(null=True, blank=True, max_length=255, verbose_name=_('Youtube video url'))
    image = models.FileField(upload_to='gallery/', blank=True, verbose_name=_('Good practices'))
    caption = models.TextField(blank=True, verbose_name=_('Caption'), null=True)
    good_practice = models.ForeignKey(
        'good_practice.GoodPractice', related_name='good_practice', on_delete=models.PROTECT,
        verbose_name=_('Good practice'), null=True, blank=True
    )
    is_published = models.BooleanField(
        default=False, verbose_name=_('Is published?')
    )

    class Meta:
        verbose_name = _('Gallery')
        verbose_name_plural = _('Gallery')

    def __str__(self):
        return self.caption
