from rest_framework import viewsets, mixins
from .models import Train
from .serializers import TrainSerializer


class TrainViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin,
                   mixins.UpdateModelMixin, mixins.ListModelMixin):
    queryset = Train.objects.all()
    serializer_class = TrainSerializer

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
