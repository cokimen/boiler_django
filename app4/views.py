from rest_framework import viewsets, mixins
from .models import Fish, Ocean
from .serializers import FishSerializer, OceanSerializer


class FishViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = Fish.objects.all()
    serializer_class = FishSerializer

    def get_serializer_context(self):
        context = super(FishViewSet, self).get_serializer_context()
        return context

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class OceanViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = Ocean.objects.all()
    serializer_class = OceanSerializer

    def get_serializer_context(self):
        context = super(OceanViewSet, self).get_serializer_context()
        context.update({"pengarang": self.request.user})
        context.update({"judul": self.request.data.get('title', None)})
        context.update({'action': self.action})
        return context

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
