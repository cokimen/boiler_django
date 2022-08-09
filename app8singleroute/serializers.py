from pyexpat import model
from rest_framework import serializers

from .models import Carburator, Car


class CarburatorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Carburator
        fields = '__all__'

    def validate(self, attrs):
        # import pdb
        # pdb.set_trace()
        return super().validate(attrs)

    def create(self, validated_data):
        print('create')
        return super().create(validated_data)

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)

    def to_internal_value(self, data):
        return super().to_internal_value(data)

    def to_representation(self, instance):
        return super().to_representation(instance)
