from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
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
    lookup_field = 'id'
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)
    filterset_fields = ['id']


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
