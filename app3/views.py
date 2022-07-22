from multiprocessing import context
from coreapi import Object
from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response
# import models / entity
from .models import (PersonSample, SchoolSample)
# import serializer
from .serializers import (PersonSampleSerializer, SchoolSampleSerializer)


class PersonSampleViewSet(viewsets.GenericViewSet,
                          mixins.ListModelMixin, mixins.CreateModelMixin,
                          mixins.RetrieveModelMixin, mixins.UpdateModelMixin):
    queryset = PersonSample.objects.all()
    serializer_class = PersonSampleSerializer

    def get_serializer_class(self):
        if self.action == 'person_school':
            return SchoolSampleSerializer
        return self.serializer_class

    @action(methods=['GET', 'POST'], detail=True)
    def person_school(self, request, *args, **kwargs):
        if request.method == 'POST':
            data = self.get_serializer(data=request.data, context={
                'request': request, 'kwargs': kwargs, 'method': request.method})
            if data.is_valid():
                data.save()
                return Response(data.data)

        # liat ini
        #   person_qs.schoolsample_set.all() diganti jadi   person_qs.schoolsample_set sama aja
        schoolsample_serializer = SchoolSampleSerializer(
            [Object()], context={
                'request': request, 'kwargs': kwargs}, many=True)
        return Response({'personsamppe': schoolsample_serializer.data})

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def perform_create(self, serializer):
        return super().perform_create(serializer)

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def perform_update(self, serializer):
        return super().perform_update(serializer)
