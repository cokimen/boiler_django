from .views import BirdViewSet
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('bird', BirdViewSet, basename='bird')
urlpatterns = router.urls
