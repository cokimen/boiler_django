from rest_framework import serializers
from .models import AquaBottle, Bottle


class BottleSerializer(serializers.Serializer):
    height = serializers.DecimalField()
    width = serializers.DecimalField()
    length = serializers.DecimalField()
