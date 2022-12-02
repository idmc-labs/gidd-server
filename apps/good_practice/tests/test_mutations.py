# WIP

# import pytest
# import datetime

# from apps.country.models import Country
# from apps.good_practice.models import (
#     GoodPractice,
#     DriversOfDisplacement,
#     Tag,
#     FocusArea,
# )
# from config.utils import GraphQLTestClient, assert_num_queries


# from config.tests import TestCase


# class GoodPracticeMutation(TestCase):
#     @classmethod
#     def setUpTestData(cls):
#         cls.country1 = Country.objects.create(name='abc')
#         cls.country2 = Country.objects.create(name='xyz')
#         cls.drivers_of_displacement1 = DriversOfDisplacement.objects.create(name='driver1')
#         cls.drivers_of_displacement2 = DriversOfDisplacement.objects.create(name='driver2')
#         cls.tag1 = Tag.objects.create(name='tag1')
#         cls.tag2 = Tag.objects.create(name='tag2')
#         cls.focus_area1 = FocusArea.objects.create(name='focus_area1')
#         cls.focus_area2 = FocusArea.objects.create(name='focus_area2')

#     def test_create_goodpractice(self):
#         query = """
#             mutation CreateGoodPractice ($input: GoodPracticeInputType!) {
#                 createGoodPractice (input: $input) {
#                     ... on GoodPracticeType {
#                         title
#                         description
#                         mediaAndResourceLinks
#                         type
#                         implementingEntity
#                         stage
#                         publishedDate
#                         startYear
#                         endYear
#                         # image {
#                         #     name
#                         #     url
#                         # }
#                         countries {
#                             id
#                             iso3
#                         }
#                         driverOfDisplacement {
#                             id
#                             name
#                         }
#                         focusArea {
#                             id
#                             name
#                         }
#                         tags {
#                             id
#                             name
#                         }
#                     }
#                 }
#             }
#         """
#         input_variable = dict(
#             title="Good Practice Title",
#             # description="test description",
#             # media_and_resource_links="www.test.com",
#             countries=[self.country1.id, self.country2.id],
#             type=GoodPractice.Type.RISK_REDUCTION_AND_PREVENTION.value,
#             # implementing_entity="asdfsdfa",
#             drivers_of_displacement=[self.drivers_of_displacement1.id, self.drivers_of_displacement2.id],
#             stage=GoodPractice.StageType.PROMISING.value,
#             focus_areas=[self.focus_area1.id, self.focus_area2.id],
#             tags=[self.tag1.id, self.tag2.id],
#             # published_date=datetime.datetime.now(),
#             # image: asdfsdfa,
#             start_year=2022,
#             # end_year=2023,
#         )
#         resp = self.query_check(query, variables=input_variable)
#         print("variables:", input_variable)
#         print("Date", datetime.datetime.today())
#         print(resp)
#         assert resp['data']['title'] == 'Good Practice Title'


# @pytest.mark.django_db(transaction=True)
# def test_create_goodpractice(db, gql_client: GraphQLTestClient):
#     cls.country1 = Country.objects.create(name='abc')
#     cls.country2 = Country.objects.create(name='xyz')
#     cls.drivers_of_displacement1 = DriversOfDisplacement.objects.create(name='driver1')
#     cls.drivers_of_displacement2 = DriversOfDisplacement.objects.create(name='driver2')
#     cls.tag1 = Tag.objects.create(name='tag1')
#     cls.tag2 = Tag.objects.create(name='tag2')
#     cls.focus_area1 = Tag.objects.create(name='focus_area1')
#     cls.focus_area2 = Tag.objects.create(name='focus_area2')
#     query = """
#     mutation CreateGoodPractice ($input: CreateGoodPracticeInput!) {
#         createGoodPractice (input: $input) {
#           ... on GoodPracticeType {
#             title
#             description
#             mediaAndResourceLinks
#             type
#             implementingEntity
#             stage
#             publishedDate
#             startYear
#             endYear
#             # image {
#             #     name
#             #     url
#             # }
#             countries {
#                 id
#                 iso3
#             }
#             driverOfDisplacement {
#                 id
#                 name
#             }
#             focusArea {
#                 id
#                 name
#             }
#             tags {
#                 id
#                 name
#             }
#           }
#         }
#       }
#     """
#     with assert_num_queries(1):
#         res = gql_client.query(
#             query,
#             {
#                 "input": dict(
#                     title="Good Practice Title",
#                     # description="test description",
#                     # media_and_resource_links="www.test.com",
#                     countries=[self.country1.id, self.country2.id],
#                     type=GoodPractice.Type.RISK_REDUCTION_AND_PREVENTION.value,
#                     # implementing_entity="asdfsdfa",
#                     drivers_of_displacement=[self.drivers_of_displacement1.id, self.drivers_of_displacement2.id],
#                     stage=GoodPractice.StageType.PROMISING.value,
#                     focus_areas=[self.focus_area1.id, self.focus_area2.id],
#                     tags=[self.tag1.id, self.tag2.id],
#                     # published_date=datetime.datetime.now(),
#                     # image: asdfsdfa,
#                     start_year=2022,
#                     # end_year=2023,
#                 )
#             },
#         )
#         assert res.data == {
#             "createProject": {
#                 "title": "Good Practice Title",
#                 # "cost": None,
#                 # "dueDate": "2030-01-01T00:00:00",
#             }
#         }
