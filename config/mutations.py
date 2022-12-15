import strawberry
from typing import Optional, TypeVar, Generic
from strawberry_utils.error_types import CustomErrorType

MutationVar = TypeVar('MutationVar')


@strawberry.type
class MutationResponse(Generic[MutationVar]):
    ok: bool
    errors: Optional[CustomErrorType]
    data: Optional[MutationVar]
