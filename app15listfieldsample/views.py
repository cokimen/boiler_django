from rest_framework import viewsets, mixins
from .models import Bird, Pigeon
from .serializers import BirdSerializer, PigeonSerializer


class BirdViewSet(viewsets.GenericViewSet, mixins.ListModelMixin,
                  mixins.CreateModelMixin):
    queryset = Bird.objects.all()
    serializer_class = BirdSerializer

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def perform_create(self, serializer):
        return super().perform_create(serializer)
