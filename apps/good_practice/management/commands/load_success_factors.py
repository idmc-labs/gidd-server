from django.core.management.base import BaseCommand
from apps.good_practice.models import SuccessFactor


class Command(BaseCommand):
    help = 'Add predefined SuccessFactor instances for Good Practice'

    def handle(self, *args, **options):
        predefined_success_factors = [
            "Multi-year funding",
            "Multi-sectoral approach",
            "Community-led approach",
            "Participatory design",
            "Unearmarked funding",
            "Conflict-sensitive approach",
        ]

        for factor_name in predefined_success_factors:
            success_factor, created = SuccessFactor.objects.get_or_create(name=factor_name)
            if created:
                self.stdout.write(self.style.SUCCESS(f'SuccessFactor "{factor_name}" created'))
            else:
                self.stdout.write(self.style.SUCCESS(f'SuccessFactor "{factor_name}" already exists'))
