from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
import csv
from django.http import HttpResponse
from .models import Country, Conflict, Disaster, CountryAdditionalInfo
from .serializers import (
    CountrySerializer,
    ConflictSerializer,
    DisasterSerializer,
    CountryAdditionalInfoSerializer
)


class CountryViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CountrySerializer
    queryset = Country.objects.all().prefetch_related('country_additonal_info')
    lookup_field = 'iso3'
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)
    filterset_fields = ['id']

    @action(
        detail=True,
        methods=["get"],
        url_path="conflict-export",
        permission_classes=[AllowAny],
    )
    def conflict_export(self, request, iso3=None):
        """
        Export conflict
        """
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="conflict-data.csv"'
        writer = csv.writer(response, delimiter=',')
        writer.writerow([
            'Year', 'Total Displacement', 'Total Displacement Source', 'New Displacement', 'New Displacement Source',
            'Returns', 'Returns Source', 'Local Integration', 'Local Integration Source', 'Resettlement',
            'Resettlement Source', 'Cross border flight', 'Cross Border Flight Source', 'Children Born To IDPs',
            'Children Born To IDPS Source', 'Idp Deaths', 'Idp Deaths Source', 'Total Displacement Since',
            'New Displacement Since', 'Returns Since', 'Resettlement Since', 'Local Integration Since',
            'Cross Border Flight Since', 'Children Born To IDPS Since', 'IDP deaths since'
        ])
        conflict_qs = Conflict.objects.filter(country__iso3=iso3)
        for conflict in conflict_qs:
            writer.writerow(
                [
                    conflict.year,
                    conflict.total_displacement,
                    conflict.total_displacement_source,
                    conflict.new_displacement,
                    conflict.new_displacement_source,
                    conflict.returns,
                    conflict.returns_source,
                    conflict.local_integration,
                    conflict.local_integration_source,
                    conflict.resettlement,
                    conflict.resettlement_source,
                    conflict.cross_border_flight,
                    conflict.cross_border_flight_source,
                    conflict.children_born_to_idps,
                    conflict.children_born_to_idps_source,
                    conflict.idp_deaths,
                    conflict.idp_deaths_source,
                    conflict.total_displacement_since,
                    conflict.new_displacement_since,
                    conflict.returns_since,
                    conflict.resettlement_since,
                    conflict.local_integration_since,
                    conflict.cross_border_flight_since,
                    conflict.children_born_to_idps_since,
                    conflict.idp_deaths_since,
                ]
            )
        return response

    @action(
        detail=True,
        methods=["get"],
        url_path="disaster-export",
        permission_classes=[AllowAny],
    )
    def disaster_export(self, request, iso3=None):
        """
        Export disaster
        """
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="disaster-data.csv"'
        writer = csv.writer(response, delimiter=',')
        writer.writerow([
            'Year', 'Glide Number', 'Event Name', 'Location Text', 'Start Date', 'Start Date Accuracy',
            'End Date', 'End Date Accuracy', 'Hazard Category', 'Hazard Sub Category', 'Hazard Sub Category',
            'Hazard Sub Type', 'Hazard Type', 'New Displacement', 'New Displacement Source', 'New Displacement Since'
        ])
        disaster_qs = Disaster.objects.filter(country__iso3=iso3)
        for disaster in disaster_qs:
            writer.writerow(
                [
                    disaster.year,
                    disaster.glide_number,
                    disaster.event_name,
                    disaster.location_text,
                    disaster.start_date,
                    disaster.start_date_accuracy,
                    disaster.end_date,
                    disaster.end_date_accuracy,
                    disaster.hazard_category,
                    disaster.hazard_sub_category,
                    disaster.hazard_sub_type,
                    disaster.hazard_type,
                    disaster.new_displacement,
                    disaster.new_displacement_source,
                    disaster.new_displacement_since,
                ]
            )
        return response


class CountryAdditionalInfoViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CountryAdditionalInfoSerializer
    queryset = CountryAdditionalInfo.objects.all().select_related('country')
    lookup_field = 'id'
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)
    filterset_fields = ['id']


class ConflictViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ConflictSerializer
    queryset = Conflict.objects.all().select_related('country').prefetch_related('country__country_additonal_info')
    lookup_field = 'id'
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)
    filterset_fields = ['id']


class DisasterViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = DisasterSerializer
    queryset = Disaster.objects.all().select_related('country').prefetch_related('country__country_additonal_info')
    lookup_field = 'id'
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)
    filterset_fields = ['id']
