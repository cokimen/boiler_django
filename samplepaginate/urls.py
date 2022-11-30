from email.mime import base
from rest_framework.routers import DefaultRouter
from .views import DrinkViewSet

router = DefaultRouter()


router.register('drink', DrinkViewSet, basename='drink')

urlpatterns = []+router.urls
