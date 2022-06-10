
from apps.country.models import (
    CountryAdditionalInfo, OverView, Country
)
from django.db.models import Count
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


def country_overviews_load(keys: List[int]):
    qs = OverView.objects.filter(
        country_id__in=keys, is_published=True,
    )

    _map = defaultdict(list)
    for country_overview in qs:
        _map[country_overview.country.id].append(country_overview)
    return [_map[key] for key in keys]


def good_practices_count_load(keys: List[int]):
    qs = Country.objects.filter(id__in=keys, country_good_practice__is_published=True).annotate(
        good_practices_count=Count('country_good_practice')
    ).values('id', 'good_practices_count')
    _map = defaultdict(int)
    for country in qs:
        _map[country['id']] = country['good_practices_count']
    return [_map[key] for key in keys]


load_country_additonal_info = sync_to_async(country_additonal_info_load)
load_country_overviews = sync_to_async(country_overviews_load)
load_good_practices_count = sync_to_async(good_practices_count_load)
