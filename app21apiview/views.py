from rest_framework import viewsets
from .models import Cosmos
from rest_framework.decorators import api_view
from .serializers import CosmosSerializer
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'POST'])
def CosmosApiView(request, *args, **kwargs):
    _queryset = Cosmos.objects.all()
    if request.method == 'POST':
        _serializer = CosmosSerializer(data=request.data, many=False)
        if _serializer.is_valid():
            _serializer.save()
            return Response(_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        data = CosmosSerializer(_queryset, many=True)
        return Response(
            data.data,
            status=status.HTTP_200_OK
        )


def trial(pk):
    try:
        data = Cosmos.objects.get(pk=pk)
        return data
    except Cosmos.DoesNotExist:
        return None
        # return Cosmos()
