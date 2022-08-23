from rest_framework import serializers
from .models import Cosmos


class CosmosSerializer(serializers.Serializer):
    galaxy_group = serializers.CharField()

    def validate(self, attrs):
        return super().validate(attrs)

    # will execute if save executed usually
    # binding to post method
    def create(self, validated_data):
        return Cosmos.objects.create(**validated_data)

    def to_representation(self, instance):
        # you can return dict as type
        # instance type is not mandatory
        return {
            "group galaxynya": instance.galaxy_group
        }
