from django.apps import AppConfig


class GoodPracticeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.good_practice'
    verbose_name = "Global Repository of Good Practices"
