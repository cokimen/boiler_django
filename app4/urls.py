from .views import FishViewSet, OceanViewSet
from rest_framework.routers import DefaultRouter
router = DefaultRouter()

router.register('fish', FishViewSet, basename='fish')
router.register('ocean', OceanViewSet, basename='ocean')
urlpatterns = router.urls
