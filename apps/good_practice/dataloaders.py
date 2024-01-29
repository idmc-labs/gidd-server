from apps.good_practice.models import Gallery, GoodPractice
from apps.country.models import Country
from collections import defaultdict
from typing import List
from asgiref.sync import sync_to_async


def gallery_load(keys: List[int]):
    qs = Gallery.objects.filter(
        good_practice__in=keys,
        is_published=True,
    )

    _map = defaultdict(list)
    for gallery in qs:
        _map[gallery.good_practice.id].append(gallery)
    return [_map[key] for key in keys]


def good_practice_country_load(keys: List[int]):
    qs = Country.objects.filter(country_good_practice__in=keys)

    _map = defaultdict(list)
    for country in qs:
        for c in country.country_good_practice.all():
            _map[c.id].append(country)
    return [_map[key] for key in keys]


def good_practice_image_load(keys: List[int]):
    qs = GoodPractice.objects.filter(id__in=keys)
    _map = defaultdict(list)
    for good_practice in qs:
        _map[good_practice.id].append(good_practice.image)
    return [_map[key] for key in keys]


def good_practice_tag_load(keys: List[int]):
    qs = GoodPractice.objects.filter(id__in=keys)
    _map = defaultdict(list)
    for good_practice in qs:
        for tag in good_practice.tags.all():
            _map[good_practice.id].append(tag)
    return [_map[key] for key in keys]


def good_practice_driver_of_displacement_load(keys: List[int]):
    qs = GoodPractice.objects.filter(id__in=keys)
    _map = defaultdict(list)
    for good_practice in qs:
        for driver_of_displacement in good_practice.drivers_of_displacement.all():
            _map[good_practice.id].append(driver_of_displacement)
    return [_map[key] for key in keys]


def good_practice_focus_area_load(keys: List[int]):
    qs = GoodPractice.objects.filter(id__in=keys)
    _map = defaultdict(list)
    for good_practice in qs:
        for focus_area in good_practice.focus_area.all():
            _map[good_practice.id].append(focus_area)
    return [_map[key] for key in keys]


def good_practice_success_factor_load(keys: List[int]):
    qs = GoodPractice.success_factor.through.objects.filter(goodpractice__in=keys).select_related('successfactor')
    _map = defaultdict(list)
    for instance in qs:
        _map[instance.goodpractice_id].append(instance.successfactor)
    return [_map[key] for key in keys]


load_gallery = sync_to_async(gallery_load)
load_good_practice_country = sync_to_async(good_practice_country_load)
load_good_practice_image = sync_to_async(good_practice_image_load)
load_good_practice_tags = sync_to_async(good_practice_tag_load)
load_good_practice_driver_of_displacement = sync_to_async(
    good_practice_driver_of_displacement_load
)
load_good_practice_focus_area = sync_to_async(good_practice_focus_area_load)
load_good_practice_success_factor = sync_to_async(
    good_practice_success_factor_load
)
