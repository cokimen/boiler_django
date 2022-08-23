from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import CosmosApiView
router = DefaultRouter()

urlpatterns = router.urls
urlpatterns += [
    path('cosmos/', CosmosApiView),
]
