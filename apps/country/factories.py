
import factory
from factory import fuzzy
from factory.django import DjangoModelFactory

from .models import Country, Continent, Region, SubRegion
# from .serializers import CountrySerializer


# PROFILE_FIELDS = ['display_picture', 'organization', 'language', 'email_opt_outs', 'last_active_project']


class CountryFactory(DjangoModelFactory):
    name = factory.Faker('test-country')
    iso3 = fuzzy.FuzzyText(length=15)
    iso2 = fuzzy.FuzzyText(length=15)
    idmc_names = fuzzy.FuzzyText(length=15)
    idmc_continent = factory.Faker(Continent.EUROPE)
    idmc_region = factory.Faker(Region.SOUTH_EAST_ASIA)
    idmc_sub_region = factory.Faker(SubRegion.CARRIBEAN)
    wb_region = fuzzy.FuzzyText(length=15)
    un_population_division_names = fuzzy.FuzzyText(length=15)
    united_nations_regions = factory.Faker(Region.SOUTH_EAST_ASIA)
    is_least_developed_country = True
    is_small_island_developing_state = True
    is_idmc_go_2013 = False
    is_conflict_affected_since_1970 = True
    is_country_office_nrc = True
    is_country_office_iom = True

    class Meta:
        model = Country

    # first_name = factory.Faker('first_name')
    # last_name = factory.Faker('last_name')
    # email = factory.Sequence(lambda n: f'{n}@xyz.com')
    # username = factory.LazyAttribute(lambda user: user.email)
    # password_text = fuzzy.FuzzyText(length=15)
    # password = factory.PostGeneration(lambda user, *args, **kwargs: user.set_password(user.password_text))

    # class Meta:
    #     model = User

    # @classmethod
    # def _create(cls, model_class, *args, **kwargs):
    #     password_text = kwargs.pop('password_text')
    #     profile_data = {
    #         key: kwargs.pop(key) for key in PROFILE_FIELDS if key in kwargs
    #     }
    #     user = super()._create(model_class, *args, **kwargs)
    #     UserSerializer.update_or_create_profile(user, profile_data)
    #     user.profile.refresh_from_db()
    #     user.password_text = password_text
    #     return user


# class FeatureFactory(DjangoModelFactory):
#     title = factory.PostGeneration(lambda feature, *args, **kwargs: f'Feature {feature.key}')
#     feature_type = fuzzy.FuzzyChoice(Feature.FeatureType.choices, getter=lambda c: c[0])

#     class Meta:
#         model = Feature