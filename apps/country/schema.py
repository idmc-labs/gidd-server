import strawberry
from typing import List
from .types import (
    ConflictType,
    DisasterType,
    CountryType,
    ConflictListType,
    DisasterListType,
    CountryListType,
    DisasterStatisticsType,
    TimeSeriesStatisticsType,
    CategoryStatisticsType,
    ConflictStatisticsType,
)
from apps.country.models import Disaster, Conflict
from django.db.models import Value, Sum, F, Count, CharField, Case, When
from .gh_filters import DisasterStatisticsFilter, ConflictStatisticsFilter
from strawberry_django.filters import apply as filter_apply
from asgiref.sync import sync_to_async


@sync_to_async
def disaster_statistics_qs(disaster_qs) -> List[DisasterStatisticsType]:
    timeseries_qs = disaster_qs.values('year').annotate(
        total=Sum('new_displacement')
    ).values('year', 'total')

    categories_qs = disaster_qs.values('hazard_category').annotate(
        total=Sum('new_displacement'),
        label=Case(
            When(hazard_sub_category=None, then=Value('Not labeled')),
            default=F('hazard_sub_category'),
            output_field=CharField()
        )
    ).values('label', 'total')
    return [
        DisasterStatisticsType(
            new_displacements=disaster_qs.aggregate(
                total_new_displacement=Sum('new_displacement')
            )['total_new_displacement'],

            total_events=disaster_qs.values('event_name').annotate(
                events=Count('id')
            ).aggregate(total_events=Sum('events'))['total_events'],

            timeseries=[TimeSeriesStatisticsType(**item) for item in timeseries_qs],

            categories=[CategoryStatisticsType(**item) for item in categories_qs]
        )
    ]


@sync_to_async
def conflict_statistics_qs(conflict_qs) -> List[ConflictStatisticsType]:
    timeseries_qs = conflict_qs.values('year').annotate(
        total=Sum('new_displacement')
    ).values('year', 'total')
    return [
        ConflictStatisticsType(
            total_idps=conflict_qs.aggregate(
                total_new_displacement=Sum('new_displacement')
            )['total_new_displacement'],

            new_displacements=conflict_qs.aggregate(
                total_new_displacement=Sum('new_displacement')
            )['total_new_displacement'],

            timeseries=[TimeSeriesStatisticsType(**item) for item in timeseries_qs],
        )
    ]


@strawberry.type
class Query:
    conflicts: List[ConflictListType] = strawberry.django.field()
    disasters: List[DisasterListType] = strawberry.django.field()
    countries: List[CountryListType] = strawberry.django.field()
    conflict: ConflictType = strawberry.django.field()
    disaster: DisasterType = strawberry.django.field()
    country: CountryType = strawberry.django.field()

    @strawberry.field
    def disaster_statistics(self, filters: DisasterStatisticsFilter) -> List[DisasterStatisticsType]:
        return disaster_statistics_qs(filter_apply(filters, Disaster.objects.all()))

    @strawberry.field
    def conflict_statistics(self, filters: ConflictStatisticsFilter) -> List[ConflictStatisticsType]:
        return conflict_statistics_qs(filter_apply(filters, Conflict.objects.all()))
