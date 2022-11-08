from apps.common.models import StaticPage
from apps.common.factories import (
    StaticPageFactory,
)
from config.tests import TestCase


class CommonQueryTestCase(TestCase):
    def test_static_pages_query(self):
        query = """
            query MyQuery {
              staticPages {
                id
                type
                description
              }
            }
        """

        static_page_1 = StaticPageFactory.create(
            type=StaticPage.Type.GOOD_PRACTICE_CONTACT_INFORMATION,
        )
        static_page_1.description_fr = f'IN-FRENCH: {static_page_1.description_en}'
        static_page_1.save()
        for lang, description in [
            ('en', static_page_1.description_en),
            ('fr', static_page_1.description_fr),
        ]:
            resp = self.query_check(query, HTTP_ACCEPT_LANGUAGE=lang)
            assert [
                dict(
                    id=str(static_page_1.id),
                    type=static_page_1.type.name,
                    description=description,
                )
            ] == resp["data"]["staticPages"], (lang, static_page_1.description)
