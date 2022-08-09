from multiprocessing import context
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer

from .models import Carburator, Car
from .serializers import CarburatorSerializer


class CarView(APIView):

    # renderer_classes = [JSONRenderer]

    def __init__(self, **kwargs):
        self.number = 0
        self.serializer = CarburatorSerializer
        super().__init__(**kwargs)

    def get_format_suffix(self, **kwargs):
        print('naz', kwargs)
        return super().get_format_suffix(**kwargs)

    def get_view_name(self):
        print('view name')
        return super().get_view_name()

    def get_renderer_context(self):
        # import pdb
        # pdb.set_trace()
        print('get_renderer_context open')
        self.number += 1
        print(self.number, "get_renderer_context close")
        print(self.request.method, "check method")

        if self.request.method == 'GET':
            print('ookde')
        return super().get_renderer_context()

    def get_parsers(self):
        # import pdb
        # pdb.set_trace()
        print('getparser')
        print('execute get_renderers')
        return super().get_parsers()

    def get_renderers(self):
        return super().get_renderers()

    def get(self, request, format=None):
        print('get open')
        self.number += 1
        print(self.number, "get close")
        return Response({'get': 'get'})

    # seharusnya didef post tidak perlud ada args dan kwargs cuma jika ingin dipass dan ternyata
    # dari proses sebelumnya tidak dipass maka perlu dikasih default value yaitu None
    def post(self, request, args=None, kwargs=None, format=None):
        print('post open')
        self.number += 1
        print(self.number, "post close")

        _serializer = CarburatorSerializer(data=request.data,
                                           context={'request': request})
        if _serializer.is_valid():
            _serializer.save()
        else:
            return Response({'error': _serializer.error_messages})

        # bisa override to representation tapi property valunye gudah gak bisa disave lagi ke database
        _serializer.instance.id = 9000000000
        _serializer.to_representation(_serializer.instance)
        return Response({'post': _serializer.data})

    def patch(self, request, format=None):
        print('patch open')
        self.number += 1
        print(self.number, "patch close")
        return Response({'patch': 'patch'})
