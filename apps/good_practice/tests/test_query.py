from django.utils import translation
from modeltranslation.utils import build_localized_fieldname

from apps.good_practice.factories import GoodPracticeFactory
from config.tests import TestCase


class GoodPracticeQueryTestCase(TestCase):
    def test_good_practices_query(self):
        query = """
            query MyQuery {
              goodPractices(pagination: {limit: 10}, ordering: {id: ASC}) {
                totalCount
                results {
                  id
                  title
                  description
                  mediaAndResourceLinks
                  type
                  typeLabel
                  stage
                  stageLabel
                }
              }
            }
        """
        good_practices = GoodPracticeFactory.create_batch(3, is_published=True)
        text_lang_fields = (
            "title",
            "description",
            "media_and_resource_links",
        )
        for good_practice in good_practices[:2]:
            for field in text_lang_fields:
                for lang in self.TEST_LANGUAGES[1:]:
                    setattr(
                        good_practice,
                        build_localized_fieldname(field, lang),
                        f"[{lang}] {getattr(good_practice, field)}",
                    )
            good_practice.save()
        GoodPracticeFactory.create(is_published=False)
        for lang in self.TEST_LANGUAGES:
            resp = self.query_check(query, HTTP_ACCEPT_LANGUAGE=lang)
            with translation.override(lang):
                assert {
                    "totalCount": 3,
                    "results": [
                        dict(
                            id=str(gp.id),
                            title=gp.title,
                            description=gp.description,
                            mediaAndResourceLinks=gp.media_and_resource_links,
                            type=gp.type,
                            typeLabel=gp.type,
                            stage=gp.stage,
                            stageLabel=gp.stage,
                        )
                        for gp in good_practices
                    ],
                } == resp["data"]["goodPractices"]
