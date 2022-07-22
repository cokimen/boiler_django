from rest_framework import viewsets
# import model
from .models import (Game, GameDetail)

from .serializers import (GameSerializer, GameDetailSerializer)


class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

    def get_serializer_class(self):
        return self.serializer_class


class GameDetailViewSet(viewsets.ModelViewSet):
    queryset = GameDetail.objects.all()
    serializer_class = GameDetailSerializer

    def get_serializer_class(self):
        return self.serializer_class
