from rest_framework import serializers

from .models import GoodPractice


class GoodPracticeSerializer(serializers.ModelSerializer):

    class Meta:
        model = GoodPractice
        fields = '__all__'

    # def validate_old_password(self, password) -> str:
    #     if not self.instance.check_password(password):
    #         raise serializers.ValidationError('The password is invalid.')
    #     return password

    # def save(self, **kwargs):
    #     self.instance.save()
