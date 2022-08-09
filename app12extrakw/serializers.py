from rest_framework import serializers
from .models import Train


class TrainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Train
        fields = '__all__'
        extra_kwargs = {
            "country_manufacture": {
                # "write_only": True,
                "read_only": True,
            }
        }

    def validate(self, attrs):
        return super().validate(attrs)

    def create(self, validated_data):
        payload = validated_data.copy()
        payload['country_manufacture'] = 'override in create process'
        instance = Train.objects.create(**payload)
        return instance
