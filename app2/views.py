from rest_framework import viewsets
# import models
from .models import (Person, School)

# import serializers
from .serializers import (PersonSerialiser, SchoolSerializer)


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerialiser

    def get_queryset(self):
        return self.queryset

    def get_serializer_class(self):
        return self.serializer_class


class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer

    def get_queryset(self):
        return self.queryset

    def get_serializer_class(self):
        return self.serializer_class
