from rest_framework import serializers
from .models import Handphone


class HandPhoneSerializer(serializers.Serializer):
    name = serializers.CharField()
    manufacture = serializers.CharField()
    location = serializers.CharField()

    class Meta:
        fields = ('name', 'manufacture', 'location')

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret.pop('manufacture', None)
        return ret
