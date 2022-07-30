from rest_framework import serializers

# impo models
from .models import Fish, Ocean


class FishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fish
        fields = '__all__'

    def validate(self, attrs):
        return super().validate(attrs)

    def create(self, validated_data):
        return super().create(validated_data)


class OceanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ocean
        fields = '__all__'

    # hanya digunakn untuk deserialize
    def validate(self, attrs):
        _action = self.context.get('action')
        if _action == "create":
            print("okedeh")
        # if ini tidak akan tereksekusi karena deserialize
        if _action == "list":
            print("ini list didef validate")
        return super().validate(attrs)

    def create(self, validated_data):
        return super().create(validated_data)

    def to_representation(self, instance):
        _action = self.context.get('action')
        print("method ", self.context.get('request').method)
        if _action == "list":
            instance.color_water = "dioverride saat get list"
            print("ini list didef to_representation")
        if _action == "create":
            instance.color_water = "dioverride setelah create ke get"
            print("ini create didef to_representation")
        return super().to_representation(instance)
