from rest_framework.routers import DefaultRouter
from .views import AnonViewSet
router = DefaultRouter()
router.register('anon', AnonViewSet, basename='anon')
urlpatterns = router.urls
