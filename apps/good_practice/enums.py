from strawberry.enum import _process_enum
from .models import GoodPractice

TypeEnum = _process_enum(
    GoodPractice.Type, "TypeEnum", "Good practice types"
)
DriversOfDisplacementTypeEnum = _process_enum(
    GoodPractice.DriversOfDisplacementType,
    "DriversOfDisplacementTypeEnum",
    "Drivers of displacement type"
)
StageTypeEnum = _process_enum(
    GoodPractice.StageType,
    "StageTypeEnum",
    "Stage types"
)
FocusAreaEnum = _process_enum(
    GoodPractice.FocusArea,
    "FocusAreaEnum",
    "Focus area"
)
