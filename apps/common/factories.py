from factory import fuzzy
from factory.django import DjangoModelFactory

from .models import StaticPage


class StaticPageFactory(DjangoModelFactory):
    description = fuzzy.FuzzyText(length=50)

    class Meta:
        model = StaticPage
