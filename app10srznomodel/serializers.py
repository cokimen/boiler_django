from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from .models import Tree


class TreeSerializer(serializers.Serializer):
    ordo = serializers.CharField(max_length=10)
    genus = serializers.CharField(max_length=10)

    class Meta:
        # ToDo items belong to a parent list, and have an ordering defined
        # by the 'position' field. No two items in a given list may share
        # the same position.
        model = Tree
        fields = '__all__'
        validators = [
            UniqueTogetherValidator(
                queryset=Tree.objects.all(),
                fields=['ordo', 'genus']
            )
        ]

    def validate(self, attrs):
        return super().validate(attrs)

    def create(self, validated_data):
        # return Tree.objects.create(**validated_data)
        # creaate tetap menggunakan model dari meta
        return super().create(validated_data)

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)


class TreeSerializerNoModel(serializers.Serializer):
    ordo = serializers.CharField(max_length=10)
    genus = serializers.CharField(max_length=10)

    class Meta:
        # ToDo items belong to a parent list, and have an ordering defined
        # by the 'position' field. No two items in a given list may share
        # the same position.
        fields = '__all__'
        validators = [
            UniqueTogetherValidator(
                queryset=Tree.objects.all(),
                fields=['ordo', 'genus']
            )
        ]

    def validate(self, attrs):
        return super().validate(attrs)

    def create(self, validated_data):
        return Tree.objects.create(**validated_data)

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)
