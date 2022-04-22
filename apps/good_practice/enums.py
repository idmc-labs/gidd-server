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
TriggerTypeEnum = _process_enum(
    GoodPractice.TriggerType,
    "TriggerTypeEnum",
    "Good practice trigger types"
)
DisplacementImpactTypeEnum = _process_enum(
    GoodPractice.DisplacementImpactType,
    "DisplacementImpactTypeEnum",
    "Displacement impact types"
)
InterventionPhaseTypeEnum = _process_enum(
    GoodPractice.InterventionPhaseType,
    "InterventionPhaseTypeEnum",
    "Intervention phase types"
)
StageTypeEnum = _process_enum(
    GoodPractice.StageType,
    "StageTypeEnum",
    "Stage types"
)
TimeframeTypeEnum = _process_enum(
    GoodPractice.TimeframeType,
    "TimeframeTypeEnum",
    "Timeframe type"
)
