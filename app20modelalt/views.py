from rest_framework.viewsets import generics, mixins
from .models import Property
from .serializers import PropertySerializer


class OkeViewSet(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
