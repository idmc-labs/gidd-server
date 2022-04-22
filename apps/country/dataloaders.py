
from apps.country.models import (
    CountryAdditionalInfo, OverView,
    EssentialLink, ContactPerson
)
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
        country_id__in=keys
    )

    _map = defaultdict(list)
    for country_overview in qs:
        _map[country_overview.country.id].append(country_overview)
    return [_map[key] for key in keys]


def country_essential_links_load(keys: List[int]):
    qs = EssentialLink.objects.filter(
        country_id__in=keys
    )

    _map = defaultdict(list)
    for country_essential_link in qs:
        _map[country_essential_link.country.id].append(country_essential_link)
    return [_map[key] for key in keys]


def country_contact_persons_load(keys: List[int]):
    qs = ContactPerson.objects.filter(
        country_id__in=keys
    )

    _map = defaultdict(list)
    for country_contact_person in qs:
        _map[country_contact_person.country.id].append(country_contact_person)
    return [_map[key] for key in keys]


load_country_essential_links = sync_to_async(country_essential_links_load)
load_country_additonal_info = sync_to_async(country_additonal_info_load)
load_country_overviews_load = sync_to_async(country_overviews_load)
load_country_contact_persons = sync_to_async(country_contact_persons_load)
