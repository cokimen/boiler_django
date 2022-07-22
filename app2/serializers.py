from .models import (Person, School)
from rest_framework import serializers
from django.db import transaction
# import models


class PersonSerialiser(serializers.ModelSerializer):

    class Meta:
        model = Person
        fields = '__all__'

    def create(self, validated_data):
        schools = self.context.get('request').data.get('schools')
        person = Person.objects.create(**validated_data)
        for x in schools:
            instance_school = School()
            instance_school.school_name = x.get("school_name")
            instance_school.school_level = x.get("school_level")
            instance_school.person = person
            instance_school.save()
        return person

    def to_representation(self, instance):
        schools = School.objects.filter(pk=instance.id)
        return {
            "firstname": instance.firstname,
            "lastname": instance.lastname,
            "birth_date": instance.birth_date,
            "schools": [{"school_name": x.school_name, "school_level": x.school_level} for x in schools]
        }


class SchoolSerializer(serializers.ModelSerializer):
    person = PersonSerialiser(many=False)

    class Meta:
        model = School
        fields = '__all__'

    def create(self, validated_data):
        return super().create(validated_data)
