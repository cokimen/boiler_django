from rest_framework import serializers
from .models import Bird, Pigeon
from django.db import transaction


class BirdSerializer(serializers.Serializer):

    # custom field for json template or form template is get from here
    # if you dont using modelserializer
    yf = serializers.IntegerField(source='year_found')
    sc = serializers.CharField(source='species_name')
    pg = serializers.ListField()

    @transaction.atomic
    def create(self, validated_data):
        valid_data = validated_data.copy()
        valid_data.pop('pg')
        bird = Bird.objects.create(**valid_data)
        pigeon_list = dict([])

        for x in validated_data.get("pg", []):
            pigeon = Pigeon()
            pigeon.bird = bird
            pigeon.sex = x.get('kelamin', None)
            pigeon.save()

        return bird

    def validate(self, attrs):
        return attrs

    def to_internal_value(self, data):
        return super().to_internal_value(data)

    def to_representation(self, instance):
        return {
            "year_found": instance.year_found,
            "species_name": instance.species_name
        }


class PigeonSerializer(serializers.Serializer):
    bird = serializers.PrimaryKeyRelatedField(queryset=Bird.objects.all())
    sex = serializers.CharField()

    def validate(self, attrs):
        return super().validate(attrs)

    def to_internal_value(self, data):
        return super().to_internal_value(data)

    def to_representation(self, instance):
        return super().to_representation(instance)
