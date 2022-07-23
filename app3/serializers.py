from rest_framework import serializers

# import models / Entity
from .models import (PersonSample, SchoolSample)


class PersonSampleSerializer(serializers.Serializer):
    firstname = serializers.CharField(max_length=200)
    lastname = serializers.CharField(max_length=400)
    birth_date = serializers.DateField()

    def validate(self, attrs):
        # import pdb
        # pdb.set_trace()
        return super().validate(attrs)

    def create(self, validated_data):
        schools = self.context.get('request').data.get('schools')
        person = PersonSample.objects.create(**validated_data)
        return person

    def to_representation(self, instance):
        return super().to_representation(instance)


class SchoolSampleSerializer(serializers.Serializer):
    school_name = serializers.CharField(max_length=200)
    school_level = serializers.CharField(max_length=50)

    def create(self, validated_data):
        # import pdb
        # pdb.set_trace()
        self.context.get('request').data

        school_name = self.context.get('request').data.get("school_name")
        school_level = self.context.get('request').data.get("school_level")
        personsample_id = self.context.get('kwargs').get("pk")
        instance_personsample = PersonSample.objects.get(pk=personsample_id)
        schoolsample = SchoolSample()
        schoolsample.school_name = school_name
        schoolsample.school_level = school_level
        schoolsample.person = instance_personsample
        schoolsample.save()
        return schoolsample

    def to_representation(self, instance):
        personsample_id = self.context.get('kwargs').get("pk")
        instance_personsample = PersonSample.objects.get(pk=personsample_id)
        schools = SchoolSample.objects.filter(person=instance_personsample)
        if self.context.get('method') == 'POST':
            return {
                "school_name": instance.school_name,
                "school_level": instance.school_level
            }
        return [
            {
                "id": x.pk,
                "school_name": x.school_name,
                "school_level": x.school_level
            } for x in schools
        ]

    def validate(self, attrs):
        return super().validate(attrs)
