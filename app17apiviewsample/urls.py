from .views import ClothesViewSet, ClothesViewSetList
from django.urls import path, include
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
# router.register('clo', ClothesViewSetList.as_view(), basename='clo')


urlpatterns = [
    path("clothes/", ClothesViewSet.as_view()),
    path("clo/", ClothesViewSetList.as_view()),
] + router.urls
