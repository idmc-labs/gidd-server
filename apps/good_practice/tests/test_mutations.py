import json
from django.core.files.temp import NamedTemporaryFile
from config.tests import TestCase
from apps.good_practice.factories import (
    DriversOfDisplacementFactory,
    TagFactory,
    FocusAreaFactory,
)
from country.factories import CountryFactory


class GoodPracticeMutation(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.country1 = CountryFactory.create(name="abc")
        cls.country2 = CountryFactory.create(name="xyz")

        cls.drivers_of_displacement1 = DriversOfDisplacementFactory.create(
            name="driver1"
        )
        cls.drivers_of_displacement2 = DriversOfDisplacementFactory.create(
            name="driver2"
        )

        cls.tag1 = TagFactory.create(name="tag1")
        cls.tag2 = TagFactory.create(name="tag2")

        cls.focus_area1 = FocusAreaFactory.create(name="focus_area1")
        cls.focus_area2 = FocusAreaFactory.create(name="focus_area2")

    def test_create_goodpractice(self):
        create_mutation = """
            mutation CreateGoodPractice ($input: GoodPracticeInputType!) {
              createGoodPractice(input: $input) {
                errors
                ok
                data {
                  id
                  implementingEntity
                  contactName,
                  contactEmail,
                  isTranslated
                  mediaAndResourceLinks
                  isPublished
                  pageViewedCount
                  publishedDate
                  stageLabel
                  startYear
                  endYear
                  stage
                  title
                  type
                  typeLabel
                  tags {
                    id
                    name
                  }
                  focusArea {
                    name
                    id
                  }
                  driverOfDisplacement {
                    id
                    name
                  }
                  description
                  countries {
                    id
                  }
                  underReview
                }
              }
            }
        """

        file_text = b"fake blaa"
        with NamedTemporaryFile() as t_file:
            t_file.write(file_text)
            t_file.seek(0)

            input_variable = dict(
                contactName='Rup',
                contactEmail='rup@gmail.com',
                startYear=2020,
                endYear=2020,
                type='',
                stage='',
                countries=[self.country1.id, self.country2.id],
                driversOfDisplacement=[
                    self.drivers_of_displacement1.id,
                    self.drivers_of_displacement2.id,
                ],
                focusArea=[self.focus_area1.id, self.focus_area2.id],
                tags=[self.tag1.id, self.tag2.id],
                captcha="20000000-aaaa-bbbb-cccc-000000000002",
                # En fields
                titleEn="some text title en",
                implementingEntityEn="some text implementing entity en",
                mediaAndResourceLinksEn="some text media and resource links en",
                # Fr fields
                titleFr="some text title fr",
                implementingEntityFr="some text implementing entity fr",
                mediaAndResourceLinksFr="some text media and resource links fr",
                descriptionFr="some text description fr",
                underReview=True,
                descriptionEn="""
                    <script>
                        function myFunction() {
                        document.getElementById("demo").innerHTML = "Paragraph changed.";
                        }
                    </script>
                    </head>
                    <body>

                        <h1>Demo JavaScript in Head</h1>
                        <h2> Test Heading </h2>
                        <i> Italic </i>
                        <b> Bold </b>
                        <span> Test span </span>


                        <p id="demo">A Paragraph.</p>

                        <button type="button" onclick="myFunction()">Try it</button>
                """,
            )

            response = self.client.post(
                "/graphql",
                data={
                    "operations": json.dumps(
                        {"query": create_mutation, "variables": input_variable}
                    ),
                    "t_file": t_file,
                    "map": json.dumps({"t_file": ["variables.data.image"]}),
                },
            )
            response = self.query_check(
                create_mutation, variables={"input": input_variable}
            )
            data = response["data"]["createGoodPractice"]["data"]

            # Test int fields
            self.assertEqual(input_variable["endYear"], data["endYear"])
            self.assertEqual(input_variable["startYear"], data["startYear"])

            # Test M2M fields
            country_ids = [int(item["id"]) for item in data["countries"]]
            driver_of_displacement_ids = [
                int(item["id"]) for item in data["driverOfDisplacement"]
            ]
            focus_area_ids = [int(item["id"]) for item in data["focusArea"]]
            tag_ids = [int(item["id"]) for item in data["tags"]]

            self.assertEqual(set(country_ids), set(input_variable["countries"]))
            self.assertEqual(
                set(driver_of_displacement_ids),
                set(input_variable["driversOfDisplacement"]),
            )
            self.assertEqual(set(focus_area_ids), set(input_variable["focusArea"]))
            self.assertEqual(set(tag_ids), set(input_variable["tags"]))

            # Test default translated fields
            self.assertEqual(input_variable["titleEn"], data["title"])
            self.assertEqual(
                input_variable["implementingEntityEn"], data["implementingEntity"]
            )
            self.assertEqual(
                input_variable["mediaAndResourceLinksEn"], data["mediaAndResourceLinks"]
            )
            self.assertEqual(
                input_variable["mediaAndResourceLinksEn"], data["mediaAndResourceLinks"]
            )
            expected_description = (
                "<h1>Demo JavaScript in Head</h1> <h2> Test Heading </h2> <em> Italic </em> "
                "<strong> Bold </strong>  Test span  <p>A Paragraph.</p> Try it"
            )
            self.assertEqual(data["description"].strip(), expected_description.strip())
