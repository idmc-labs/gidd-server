import strawberry
from .models import GoodPractice

TypeEnum = strawberry.enum(GoodPractice.Type, name="TypeEnum")
StageTypeEnum = strawberry.enum(GoodPractice.StageType, name="StageTypeEnum")
