from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import CarView
router = DefaultRouter()

urlpatterns = [
    path('car/', CarView.as_view()),
]
