import strawberry
from typing import TypeVar, Generic, List

GenericEnumVar = TypeVar('GenericEnumVar')


@strawberry.type
class GenericEnumValue(Generic[GenericEnumVar]):
    name: str
    label: str


def generate_enum_name_and_label(enum_class) -> List[GenericEnumValue]:
    """
    Return list of generic enum value
    """
    return [
        GenericEnumValue(
            name=enum_item.name,
            label=enum_item.label
        ) for enum_item in enum_class
    ]
