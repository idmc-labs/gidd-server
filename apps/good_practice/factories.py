from factory import fuzzy, LazyAttribute
from factory.django import DjangoModelFactory
from django.utils import timezone

from .models import (
    GoodPractice,
    Tag,
    FocusArea,
    DriversOfDisplacement,
)


class GoodPracticeFactory(DjangoModelFactory):
    title = fuzzy.FuzzyText(length=15)
    description = fuzzy.FuzzyText(length=50)
    media_and_resource_links = fuzzy.FuzzyText(length=50)
    type = ''
    stage = ''
    start_year = LazyAttribute(lambda _: timezone.now().year)

    class Meta:
        model = GoodPractice


class TagFactory(DjangoModelFactory):
    name = fuzzy.FuzzyText(length=15)

    class Meta:
        model = Tag


class FocusAreaFactory(DjangoModelFactory):
    name = fuzzy.FuzzyText(length=15)

    class Meta:
        model = FocusArea


class DriversOfDisplacementFactory(DjangoModelFactory):
    name = fuzzy.FuzzyText(length=15)

    class Meta:
        model = DriversOfDisplacement
