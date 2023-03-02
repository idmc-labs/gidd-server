import strawberry
from typing import List, Optional
from asgiref.sync import sync_to_async
from apps.good_practice.models import GoodPractice
from apps.good_practice.types import GoodPracticeType
from .serializers import GoodPracticeSerializer
from strawberry_utils.error_types import mutation_is_not_valid
from config.mutations import MutationResponse


@strawberry.type
class GoodPracticePageViewCountType:
    id: strawberry.ID
    page_viewed_count: int


@strawberry.input
class GoodPracticeInputType:
    # TODO: Use serializer to generate this type
    start_year: int
    end_year: Optional[int] = None

    # Captcha
    captcha: str

    # Enum fields
    type: Optional[str]
    stage: Optional[str]

    # M2M fields
    countries: List[strawberry.ID]
    drivers_of_displacement: Optional[List[strawberry.ID]]
    focus_area: Optional[List[strawberry.ID]]
    tags: Optional[List[strawberry.ID]]

    # English fields
    title_en: str = None
    description_en: str
    media_and_resource_links_en: Optional[str] = None
    implementing_entity_en: str

    # French fields
    title_fr: Optional[str] = None
    description_fr: Optional[str] = None
    media_and_resource_links_fr: Optional[str] = None
    implementing_entity_fr: Optional[str] = None

    contact_name: str
    contact_email: str
    what_makes_this_promising_practice: Optional[str] = None
    description_of_key_lessons_learned: Optional[str] = None
    under_review: bool


@strawberry.type
class Mutation:
    @strawberry.mutation
    @sync_to_async
    def increment_page_viewed_count(
        self, info, id: strawberry.ID
    ) -> GoodPracticePageViewCountType:
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
