from pyexpat import model
from rest_framework import serializers
from .models import Furniture


class FurnitureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Furniture
        fields = '__all__'

    def validate(self, attrs):
        print(self.context.get('action', None))
        if self.context.get('action', None) == 'update':
            print('update')
            print('self.instance = ', self.instance)
        if self.context.get('action', None) == 'create':
            print('create')
            print('self.instance = ', self.instance)
        return super().validate(attrs)

    def create(self, validated_data):
        return super().create(validated_data)

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)
