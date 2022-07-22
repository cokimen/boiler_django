from rest_framework import serializers
from django.db import transaction

# import models
from .models import (Person, School)


class PersonSerialiser(serializers.ModelSerializer):

    class Meta:
        model = Person
        fields = '__all__'

    def create(self, validated_data):
        schools = self.context.get('request').data.get('schools')
        import pdb
        pdb.set_trace()
        person = Person.objects.create(**validated_data)
        return super().create(validated_data)


class SchoolSerializer(serializers.ModelSerializer):
    person = PersonSerialiser(many=False)

    class Meta:
        model = School
        fields = '__all__'

    def create(self, validated_data):
        return super().create(validated_data)
