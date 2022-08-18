from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import OkeViewSet
router = DefaultRouter()
urlpatterns = router.urls

urlpatterns += [
    path('oke/', OkeViewSet.as_view())
]
