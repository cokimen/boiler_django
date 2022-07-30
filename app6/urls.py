from rest_framework.routers import DefaultRouter
from .views import NoClassViewSet
router = DefaultRouter()
router.register('noclassviewSet', NoClassViewSet, basename='noclassviewSet')
urlpatterns = router.urls
