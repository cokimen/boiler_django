from rest_framework import serializers
from .models import CocaCola


class CocaColaSerializer(serializers.Serializer):
    volume = serializers.IntegerField()
    series = serializers.CharField()

    def create(self, validated_data):
        return super().create(validated_data)

    def validate(self, attrs):
        return super().validate(attrs)
