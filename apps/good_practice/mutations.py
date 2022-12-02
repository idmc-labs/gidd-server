import datetime
from django.db import transaction
# from django.core.exceptions import ValidationError
from rest_framework.exceptions import ValidationError
from typing import List, Optional
from strawberry.file_uploads import Upload
from strawberry_django_plus import gql

from .enums import (
    TypeEnum,
    StageTypeEnum,
)
from config.utils import validate_hcaptcha
from apps.good_practice.models import GoodPractice
from apps.good_practice.types import GoodPracticeType


@gql.django.type(GoodPractice)
class GoodPracticePageViewCountType(gql.Node):
    id: gql.auto
    page_viewed_count: gql.auto


@gql.type
class Mutation:
    @gql.django.input_mutation
    def increment_page_viewed_count(self, info, id: gql.ID) -> GoodPracticePageViewCountType:
        obj = GoodPractice.objects.get(id=id)
        obj.page_viewed_count = obj.page_viewed_count + 1
        obj.save()
        return obj

    @gql.django.input_mutation
    def create_good_practice(
        self,
        info,
        type: TypeEnum,
        stage: StageTypeEnum,
        start_year: int,
        countries: List[int],
        drivers_of_displacement: List[int],
        focus_area: List[int],
        tags: List[int],
        end_year: Optional[int] = None,
        implementing_entity: Optional[str] = None,
        implementing_entity_fr: Optional[str] = None,
        image: Optional[Upload] = None,
        description: Optional[str] = None,
        description_fr: Optional[str] = None,
        published_date: Optional[datetime.datetime] = None,
        media_and_resource_links: Optional[str] = None,
        media_and_resource_links_fr: Optional[str] = None,
        title: Optional[str] = None,
        title_fr: Optional[str] = None,
        captcha: Optional[str] = None,
    ) -> GoodPracticeType:
        if not validate_hcaptcha(captcha):
            raise ValidationError('Captcha is invalid. Please try again')
        with transaction.atomic():
            obj = GoodPractice.objects.create(
                title=title,
                title_fr=title_fr,
                description=description,
                description_fr=description_fr,
                type=type,
                stage=stage,
                start_year=start_year,
                end_year=end_year,
                implementing_entity=implementing_entity,
                implementing_entity_fr=implementing_entity_fr,
                image=image,
                published_date=published_date,
                media_and_resource_links=media_and_resource_links,
                media_and_resource_links_fr=media_and_resource_links_fr,

            )
            obj.save()

            #  save M2m
            obj.countries.add(*countries)
            obj.tags.add(*tags)
            obj.drivers_of_displacement.add(*drivers_of_displacement)
            obj.focus_area.add(*focus_area)

            #  set is_public to true
            obj.is_public = True
            obj.save(update_fields=['is_public'])
            return obj
