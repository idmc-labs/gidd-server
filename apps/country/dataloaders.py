
from apps.country.models import CountryAdditionalInfo
from collections import defaultdict
from typing import List
from asgiref.sync import sync_to_async


def country_additonal_info_load(keys: List[int]):
    qs = CountryAdditionalInfo.objects.filter(
        country_id__in=keys
    )

    _map = defaultdict(list)
    for country_additonal_info in qs:
        _map[country_additonal_info.country.id].append(country_additonal_info)
    return [_map[key] for key in keys]


load_country_additonal_info = sync_to_async(country_additonal_info_load)
