import datetime
from django.core.files.storage import get_storage_class
import strawberry
from strawberry.enum import EnumType

StorageClass = get_storage_class()


def year_choices():
    return [(r, r) for r in range(2018, datetime.date.today().year + 1)]


def current_year():
    return datetime.date.today().year


@strawberry.type
class FileFieldType:
    name: str
    url: str

    def resolve_file(self):
        return FileFieldType(name=self.name, url=self.url)


def build_url(file, request):
    if type(file) == list:
        file = file[0]
    file_name = file.name
    url = ''
    if file_name:
        url = request.build_absolute_uri(file.url)
        return FileFieldType(name=file_name, url=url).resolve_file()
    return None


def round_and_remove_zero(num):
    if num is None or num == 0:
        return None
    absolute_num = abs(num)
    sign = 1 if num > 0 else -1
    if absolute_num <= 100:
        return sign * absolute_num
    if absolute_num <= 1000:
        return sign * round(absolute_num / 10) * 10
    if absolute_num < 10000:
        return sign * round(absolute_num / 100) * 100
    return sign * round(num / 1000) * 1000


def get_enum_label(
    enum_type: EnumType,
    value: str,
    default_description='',
) -> str:
    if value:
        return enum_type(value).label
    return default_description
