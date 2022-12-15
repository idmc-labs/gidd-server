from rest_framework import serializers
from django.db.models import ImageField
from .models import GoodPractice
from config.hcaptcha import validate_hcaptcha


class GoodPracticeSerializer(serializers.ModelSerializer):
    image = ImageField()
    captcha = serializers.CharField(required=False, allow_null=True, write_only=True)

    class Meta:
        model = GoodPractice
        fields = (
            'start_year',
            'end_year',
            'image',

            # Enum fields
            'type',
            'stage',

            # M2M fields
            'countries',
            'drivers_of_displacement',
            'focus_area',
            'tags',

            # English fields
            'title_en',
            'description_en',
            'media_and_resource_links_en',
            'implementing_entity_en',

            # French fields
            'title_fr',
            'description_fr',
            'media_and_resource_links_fr',
            'implementing_entity_fr',

            'captcha',
        )

    def validate_image(self, image):
        MAX_FILE_SIZE = 2 * 1024
        if image.size > MAX_FILE_SIZE:
            raise serializers.ValidationError("File size should be less than 2MB")

    def validate_captcha(self, captcha):
        if not validate_hcaptcha(captcha):
            raise serializers.ValidationError(
                'Invalid captcha'
            )

    def create(self, validated_data):
        drivers_of_displacements = validated_data.pop('drivers_of_displacement')
        countries = validated_data.pop('countries')
        focus_areas = validated_data.pop('focus_area')
        tags = validated_data.pop('tags')

        instance = super().create(validated_data)

        if drivers_of_displacements:
            instance.drivers_of_displacement.set(drivers_of_displacements)
        if countries:
            instance.countries.set(countries)
        if focus_areas:
            instance.focus_area.set(focus_areas)
        if tags:
            instance.tags.set(tags)
        return instance
