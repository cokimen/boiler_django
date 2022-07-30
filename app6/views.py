from rest_framework import viewsets, mixins
from rest_framework.response import Response
from django.db.models.query import QuerySet
from rest_framework.serializers import SerializerMetaclass
from boiler_django.utils import BoilerTokenAuth


class NoClassViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = [QuerySet()]
    serializer_class = SerializerMetaclass
    permission_classes = [BoilerTokenAuth]

    def create(self, request, *args, **kwargs):
        return Response({'create': 'create'})

    def list(self, request, *args, **kwargs):
        return Response({'list': 'list'})
