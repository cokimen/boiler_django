from rest_framework import serializers

# impo models
from .models import Fish, Ocean


class FishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fish
        fields = '__all__'

    def create(self, validated_data):
        return super().create(validated_data)


class OceanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ocean
        fields = '__all__'

    def create(self, validated_data):
        import pdb
        pdb.set_trace()
        return super().create(validated_data)
