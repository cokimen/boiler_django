from rest_framework import mixins, generics
from rest_framework.views import APIView
from .models import Clothes
from rest_framework.response import Response
from .serializers import ClothesSerializer


class ClothesViewSet(APIView):
    def get(self, request, format=None):
        return Response({'a': 'a'})


class ClothesViewSetList(mixins.ListModelMixin,
                         mixins.CreateModelMixin,
                         generics.GenericAPIView):
    queryset = Clothes.objects.all()
    serializer_class = ClothesSerializer

    # def get_extra_actions(self, request, *args, **kwargs):
    #     if request.method == 'get':
    #         return self.get

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
