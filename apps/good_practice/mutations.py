import strawberry
from typing import List, Optional, TypeVar, Generic
from strawberry.file_uploads import Upload
from strawberry_django_plus import gql

from .enums import (
    TypeEnum,
    StageTypeEnum,
)
from apps.good_practice.models import GoodPractice
from apps.good_practice.types import GoodPracticeType

from .serializers import GoodPracticeSerializer
from strawberry_utils.error_types import CustomErrorType, mutation_is_not_valid
from asgiref.sync import sync_to_async


MutationVar = TypeVar('MutationVar')


@strawberry.type
class MutationResponse(Generic[MutationVar]):
    ok: bool
    errors: Optional[CustomErrorType]
    data: Optional[MutationVar]


@strawberry.type
class Response:
    ok: bool
    errors: Optional[CustomErrorType]
    data: Optional[GoodPracticeType]


@strawberry.type
class GoodPracticePageViewCountType:
    id: strawberry.ID
    page_viewed_count: int


@strawberry.input
class GoodPracticeInputType:
    # TODO: Use serializer to generate this type
    start_year: int
    end_year: int

    # Enum fields
    type: TypeEnum
    stage: StageTypeEnum

    # M2M fields
    countries: List[strawberry.ID]
    drivers_of_displacement: List[strawberry.ID]
    focus_area: List[strawberry.ID]
    tags: List[strawberry.ID]

    image: Upload

    # English fields
    title_en: Optional[str] = None
    description_en: Optional[str] = None
    media_and_resource_links_en: Optional[str] = None
    implementing_entity_en: Optional[str] = None

    # French fields
    title_fr: Optional[str] = None
    description_fr: Optional[str] = None
    media_and_resource_links_fr: Optional[str] = None
    implementing_entity_fr: Optional[str] = None


@strawberry.type
class Mutation:
    @strawberry.mutation
    def increment_page_viewed_count(self, info, id: gql.ID) -> GoodPracticePageViewCountType:
        obj = GoodPractice.objects.get(id=id)
        obj.page_viewed_count = obj.page_viewed_count + 1
        obj.save()
        return obj

    @strawberry.mutation
    @sync_to_async
    def create_good_practice(
        self,
        info,
        input: GoodPracticeInputType,
    ) -> MutationResponse[GoodPracticeType]:
        data = vars(input)
        serializer = GoodPracticeSerializer(data=data)
        if errors := mutation_is_not_valid(serializer):
            return MutationResponse(errors=errors, ok=False, data=None)
        instance = serializer.save()
        return MutationResponse(errors=None, ok=True, data=instance)
