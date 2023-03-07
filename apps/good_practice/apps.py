from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class GoodPracticeConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.good_practice"
    verbose_name = _("Global Repository of Good Practices")
