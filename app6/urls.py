from rest_framework.routers import DefaultRouter
from .views import NoClassViewSet, FurnitureViewSet
router = DefaultRouter()
router.register('noclassviewSet', NoClassViewSet, basename='noclassviewSet')
router.register('furniture', FurnitureViewSet, basename='furniture')
urlpatterns = router.urls
