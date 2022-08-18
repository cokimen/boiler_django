from rest_framework.response import Response
from django.http import JsonResponse, HttpResponse
# Create your views here.


# datasimple = None


def get(request, *args, **kwargs):
    return JsonResponse({'a': 'erhan'})


def post(request, *args, **kwargs):
    return JsonResponse({'a': 'post'})


def internal_def(request):
    if request.method == 'GET':
        return JsonResponse({'a': 'GET'})
    if request.method == 'POST':
        return JsonResponse({'a': 'POST'})


class CustomBro():
    # status_code = 404
    # streaming = None
    # has_header = get
    # headers = {
    #     "setDefault": ""
    # }
    # _resource_closers = []
    # reason_phrase = []
    # items = get
    # cookies = {}

    @staticmethod
    def initial(request, *args, **kwargs):
        return CustomBro().route_control(request, *args, **kwargs)

    def route_control(self, request, *args, **kwargs):
        if request.method == 'GET':
            return self.__get_bro(request, *args, **kwargs)
        else:
            return self.__post_bro(request, *args, **kwargs)

    def __get_bro(self, request, *args, **kwargs):
        return HttpResponse({'a : __get_bro'})

    def __post_bro(self, request, *args, **kwargs):
        return JsonResponse({'a: postbro'})
