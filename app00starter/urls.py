from urllib import request
from django.urls import path, include
from .views import get, internal_def, CustomBro
urlpatterns = [
    path('basic/', get),
    path('basic1/', internal_def),
    path('basic2/', CustomBro.initial),
]
