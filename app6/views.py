from rest_framework import viewsets, mixins
from rest_framework.response import Response
from django.db.models.query import QuerySet
from boiler_django.utils import BoilerTokenAuth
from .models import Furniture
from .serializers import FurnitureSerializer


class NoClassViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = [QuerySet()]
    serializer_class = FurnitureSerializer
    permission_classes = [BoilerTokenAuth]

    def create(self, request, *args, **kwargs):
        return Response({'create': 'create'})

    def list(self, request, *args, **kwargs):
        return Response({'list': 'list'})


class FurnitureViewSet(viewsets.ModelViewSet):
    queryset = Furniture.objects.all()
    serializer_class = FurnitureSerializer
    # authentication_classes =
    # permission_classes =

    def get_serializer_context(self):
        context = super(FurnitureViewSet, self).get_serializer_context()
        # context.update({'action': self.action})
        return context

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def perform_create(self, serializer):
        return super().perform_create(serializer)

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    def perform_update(self, serializer):
        return super().perform_update(serializer)

    #

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    def perform_destroy(self, instance):
        return super().perform_destroy(instance)

    # others

    def perform_authentication(self, request):
        return super().perform_authentication(request)

    def reverse_action(self, url_name, *args, **kwargs):
        return super().reverse_action(url_name, *args, **kwargs)

    def perform_content_negotiation(self, request, force=False):
        return super().perform_content_negotiation(request, force)
