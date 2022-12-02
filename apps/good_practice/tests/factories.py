import datetime
import factory
from factory import fuzzy
from factory.django import DjangoModelFactory
from django.core.files.base import ContentFile

from apps.good_practice.models import GoodPractice


class GoodFactoryFactory(DjangoModelFactory):
    title = fuzzy.FuzzyText(length=50)
    description = fuzzy.FuzzyText(length=100)
    media_and_resource_links = fuzzy.FuzzyText(length=50)
    type = fuzzy.FuzzyText(length=50)
    implementing_entity = fuzzy.FuzzyText(length=50)
    stage = fuzzy.FuzzyText(length=50)
    published_date = fuzzy.FuzzyNaiveDateTime(datetime.datetime.now())
    image = factory.LazyAttribute(
        lambda _: ContentFile(
            factory.django.ImageField()._make_data(
                {'width': 1024, 'height': 768}
            ), 'flash_update.jpg'
        )
    )
    start_year = fuzzy.FuzzyInteger(2022, 2030)
    end_year = fuzzy.FuzzyInteger(2022, 2030)

    class Meta:
        model = GoodPractice
