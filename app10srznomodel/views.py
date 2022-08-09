from rest_framework import viewsets, mixins
from .models import Tree
from .serializers import TreeSerializer, TreeSerializerNoModel


class TreeViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin, mixins.ListModelMixin):
    queryset = Tree.objects.all()
    serializer_class = TreeSerializer

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class TreeViewSetSrzNoModel(viewsets.GenericViewSet, mixins.CreateModelMixin, mixins.ListModelMixin):
    queryset = Tree.objects.all()
    serializer_class = TreeSerializerNoModel

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
