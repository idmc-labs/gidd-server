from strawberry.enum import _process_enum
from .models import GoodPractice

TypeEnum = _process_enum(
    GoodPractice.Type, "TypeEnum", "Good practice types"
)
StageTypeEnum = _process_enum(
    GoodPractice.StageType,
    "StageTypeEnum",
    "Stage types"
)
