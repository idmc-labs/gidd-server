from django.core.management.base import BaseCommand
from strawberry.printer import print_schema
from config.schema import schema


class Command(BaseCommand):
    help = 'Create schema.graphql file'

    def handle(self, *args, **options):
        f = open("schema.graphql", "a")
        f.write(print_schema(schema))
        f.close()
        self.stdout.write(self.style.SUCCESS('schema.graphql file generated'))
