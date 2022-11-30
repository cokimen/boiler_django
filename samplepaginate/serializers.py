from rest_framework import serializers
from .models import Drink


class DrinkSerializer(serializers.Serializer):
    name = serializers.CharField()
    volumne = serializers.IntegerField()

    def validate(self, attrs):
        return super().validate(attrs)

    def create(self, validated_data):
        return Drink.objects.create(**validated_data)

    def to_representation(self, instance):
        return super().to_representation({
            "id": instance.id,
            "name": instance.name,
            "volumne": instance.volumne,
        })
