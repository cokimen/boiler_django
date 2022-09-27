from rest_framework import viewsets
from rest_framework.mixins import ListModelMixin


class DummyViewSet(viewsets.ViewSetMixin, ListModelMixin):
    pass
