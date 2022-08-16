from rest_framework import viewsets
from .models import CocaCola
from .serializers import CocaColaSerializer
from rest_framework.response import Response


class CocaColaViewSet(viewsets.ViewSet):
    queryset = CocaCola.objects.all()
    serializer = CocaColaSerializer
    lookup_field = 'series'

    def retrievecustom(self, request, *args, **kwargs):
        return Response({'a': 'a'})

    def listcustom(self, request, *args, **kwargs):
        return Response({'inilist': 'inilist'})
