from rest_framework import serializers
from .models import Clothes


class ClothesSerializer(serializers.Serializer):
    # brand_name = serializers.Serializer()
    brand_name = serializers.CharField()

    def create(self, validated_data):
        return Clothes.objects.create(**validated_data)

    def validate(self, attrs):
        return super().validate(attrs)
