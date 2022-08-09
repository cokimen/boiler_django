from rest_framework import viewsets, mixins
from .models import Handphone
from .serializers import HandPhoneSerializer


class HandphoneViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin,
                       mixins.ListModelMixin):
    queryset = Handphone.objects.all()
    serializer_class = HandPhoneSerializer

    # form untuk create

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    # view untuk list
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
