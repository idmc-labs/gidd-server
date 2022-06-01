from django.core.management.base import BaseCommand
from apps.good_practice.models import Tag


class Command(BaseCommand):
    help = 'Migrate good tags'

    def handle(self, *args, **options):
        tags = Tag.objects.bulk_create([
            Tag(name=name) for name in [
                'Annual Report',
                'Appeal',
                'Briefing Paper',
                'Country Overview',
                'Featured',
                'Global Report',
                'Mid Year Figures',
                'Quarterly Update',
            ]
        ])
        print(f'Saved {len(tags)} tags')
