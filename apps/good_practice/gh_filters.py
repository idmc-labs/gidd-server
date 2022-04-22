from django.db.models import Q

from .models import (
    GoodPractice
)
import strawberry
from .enums import (
    TypeEnum,
    DriversOfDisplacementTypeEnum,
    TriggerTypeEnum,
    DisplacementImpactTypeEnum,
    InterventionPhaseTypeEnum,
    StageTypeEnum,
    TimeframeTypeEnum,
)
from typing import List


@strawberry.django.filters.filter(GoodPractice)
class GoodPracticeFilter:
    search: str | None
    types: List[TypeEnum] | None
    drivers_of_displacements: List[DriversOfDisplacementTypeEnum] | None
    trigger_types: List[TriggerTypeEnum] | None
    displacement_impacts: List[DisplacementImpactTypeEnum] | None
    intervention_phases: List[InterventionPhaseTypeEnum] | None
    stages: List[StageTypeEnum] | None
    timeframes: List[TimeframeTypeEnum] | None
    countries: List[strawberry.ID] | None

    def filter_search(self, queryset):
        if not self.search:
            return queryset
        return queryset.filter(
            Q(title__icontains=self.search) |
            Q(description__icontains=self.search)
        )

    def filter_types(self, queryset):
        if not self.types:
            return queryset
        return queryset.filter(type__in=self.types)

    def filter_drivers_of_displacements(self, queryset):
        if not self.drivers_of_displacements:
            return queryset
        return queryset.filter(drivers_of_dispalcement=self.drivers_of_displacements)

    def filter_trigger_types(self, queryset):
        if not self.trigger_types:
            return queryset
        return queryset.filter(trigger__in=self.trigger_types)

    def filter_displacement_impacts(self, queryset):
        if not self.displacement_impacts:
            return queryset
        return queryset.filter(dispalcement_impact__in=self.displacement_impacts)

    def filter_intervention_phases(self, queryset):
        if not self.intervention_phases:
            return queryset
        return queryset.filter(intervention_phase__in=self.intervention_phases)

    def filter_stages(self, queryset):
        if not self.stages:
            return queryset
        return queryset.filter(stage__in=self.stages)

    def filter_timeframes(self, queryset):
        if not self.timeframes:
            return queryset
        return queryset.filter(timeframe__in=self.timeframes)

    def filter_countries(self, queryset):
        if not self.countries:
            return queryset
        return queryset.filter(country__in=self.countries)
