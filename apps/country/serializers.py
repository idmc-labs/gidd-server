from rest_framework import serializers
from .models import Country, CountryAdditionalInfo, Conflict, Disaster


class CountryAdditionalInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CountryAdditionalInfo
        fields = '__all__'
        lookup_field = 'id'


class CountrySerializer(serializers.ModelSerializer):
    addtional_info = CountryAdditionalInfoSerializer(many=True, source='country_additonal_info')

    class Meta:
        model = Country
        fields = '__all__'
        lookup_field = 'id'


class ConflictSerializer(serializers.ModelSerializer):
    country = CountrySerializer(many=False)

    class Meta:
        model = Conflict
        fields = '__all__'
        lookup_field = 'id'


class DisasterSerializer(serializers.ModelSerializer):
    country = CountrySerializer(many=False)

    class Meta:
        model = Disaster
        fields = '__all__'
        lookup_field = 'id'
