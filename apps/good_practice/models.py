from django.db import models
from django.utils.translation import gettext_lazy as _
from config.custom_fields import clean_text_fields


class Faq(models.Model):
    question = models.CharField(max_length=255, verbose_name=_("Question"))
    answer = models.TextField(blank=True, verbose_name=_("Answer"))
    is_published = models.BooleanField(default=False, verbose_name=_("Is published?"))

    class Meta:
        verbose_name = _("HOMEPAGE - Frequently asked question")
        verbose_name_plural = _("HOMEPAGE - Frequently asked questions")

    def __str__(self):
        return self.question


class Tag(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("Tags"))

    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")

    def __str__(self):
        return self.name


class DriversOfDisplacement(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("Name"))

    class Meta:
        verbose_name = _("Filters - Drivers of displacement")
        verbose_name_plural = _("Filters - Drivers of displacements")

    def __str__(self):
        return self.name


class FocusArea(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("Name"))

    class Meta:
        verbose_name = _("Filters - Focus area")
        verbose_name_plural = _("Filters - Focus areas")

    def __str__(self):
        return self.name


class GoodPractice(models.Model):
    class Type(models.TextChoices):
        RISK_REDUCTION_AND_PREVENTION = (
            "risk_reduction_and_prevention",
            _("Risk Reduction and Prevention (DRR, CCA and peacebuilding)"),
        )
        PROTECTION_AND_ASSISTANCE = (
            "protection_and_assistance",
            _("Protection and assistance"),
        )
        DURABLE_SOLUTIONS = (
            "durable_solutions",
            _("Durable solutions"),
        )
        STRENGTHENING_POLICY_AND_LEGAL_FRAMEWORKS = (
            "strengthening_policy_and_legal_frameworks",
            _("Strengthening policy and legal frameworks"),
        )
        GOVERNANCE_CAPACITY_AND_INSTITUTIONAL_SET_UP = (
            "governance_capacity_and_institutional_set_up",
            _("Governance capacity and institutional set-up"),
        )
        DISPLACEMENT_MONITORING = (
            "displacement_monitoring",
            _("Displacement monitoring (data collection, analysis and systems)"),
        )
        UNKNOWN = (
            "unknown",
            _("Unknown"),
        )

    class StageType(models.TextChoices):
        PROMISING = "promising", _("Promising")
        ADVANCED = "advanced", _("Advanced")
        SUCCESSFUL = "successful", _("Successful")
        UNKNOWN = "unknown", _("Unknown")

    title = models.CharField(max_length=255, verbose_name=_("Name of project"))
    description = models.TextField(
        blank=True,
        verbose_name=_("Description of the project"),
        null=True,
    )
    media_and_resource_links = models.TextField(
        blank=True,
        verbose_name=_(
            "Media and resource links (Links to any relevant reports, evaluations or other documents)"
        ),
        null=True,
    )
    countries = models.ManyToManyField(
        "country.Country",
        related_name="country_good_practice",
        verbose_name=_("Country (select from list)"),
    )
    type = models.CharField(
        max_length=255,
        verbose_name=_("Good practice type"),
        choices=Type.choices,
        blank=True,
    )
    implementing_entity = models.CharField(
        blank=True, max_length=255, verbose_name=_("Implementing organisation/entity")
    )
    drivers_of_displacement = models.ManyToManyField(
        "good_practice.DriversOfDisplacement",
        related_name="good_practice",
        verbose_name=_("Drivers of displacement"),
        blank=True,
    )
    stage = models.CharField(
        max_length=255,
        verbose_name=_("Stage"),
        choices=StageType.choices,
        null=True,
        blank=True,
    )
    focus_area = models.ManyToManyField(
        "good_practice.FocusArea",
        related_name="good_practice",
        verbose_name=_("Focus area"),
        blank=True,
    )
    tags = models.ManyToManyField(
        "good_practice.Tag",
        related_name="good_practice",
        verbose_name=_("Tags"),
        blank=True,
    )
    published_date = models.DateTimeField(blank=True, null=True)
    image = models.FileField(
        upload_to="good_practice/",
        null=True,
        blank=True,
        verbose_name=_("Good practice image"),
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created at"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Updated at"))
    is_published = models.BooleanField(default=False, verbose_name=_("Is published?"))
    start_year = models.BigIntegerField(verbose_name=_("Project start year"))
    end_year = models.BigIntegerField(
        blank=True, null=True, verbose_name=_("Project end year or ongoing")
    )
    page_viewed_count = models.BigIntegerField(
        default=0, verbose_name=_("Total page viewed count")
    )
    is_public = models.BooleanField(
        editable=False,
        default=False,
        verbose_name=_("Is public?"),
        help_text=_(
            "It indicates if a good practice is submitted without authentication."
        ),
    )
    contact_name = models.CharField(max_length=255, verbose_name=_("Contact name"), blank=True)
    contact_email = models.EmailField(max_length=255, verbose_name=_("Contact email"), blank=True)
    what_makes_this_promising_practice = models.TextField(
        verbose_name=_("What makes this a promising practice? (max 2,000 characters)"),
        blank=True,
        null=True,
        max_length=2000,
    )
    description_of_key_lessons_learned = models.TextField(
        verbose_name=_(
            "Briefly describe the key lessons learned (max 2,000 characters)"
        ),
        blank=True,
        null=True,
        max_length=2000,
    )
    under_review = models.BooleanField(default=True)

    class Meta:
        verbose_name = _("PAGES - Good practices page")
        verbose_name_plural = _("PAGES - Good practices pages")

    def __str__(self):
        return self.title

    def is_translated(self):
        return self.title_fr not in [None, ""]

    def save(self, *args, **kwargs):
        clean_text_fields(self, "description", "media_and_resource_links")
        return super().save(*args, **kwargs)


class Gallery(models.Model):
    youtube_video_url = models.URLField(
        null=True, blank=True, max_length=255, verbose_name=_("Youtube video url")
    )
    image = models.FileField(upload_to="gallery/", blank=True, verbose_name=_("Image"))
    caption = models.TextField(blank=True, verbose_name=_("Caption"), null=True)
    good_practice = models.ForeignKey(
        "good_practice.GoodPractice",
        related_name="good_practice",
        on_delete=models.CASCADE,
        verbose_name=_("Good practice"),
        null=True,
        blank=True,
    )
    is_published = models.BooleanField(default=False, verbose_name=_("Is published?"))

    class Meta:
        verbose_name = _("Gallery")
        verbose_name_plural = _("Gallery")

    def __str__(self):
        return self.caption
