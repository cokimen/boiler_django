from .views import (PersonSampleViewSet)
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('personsample', PersonSampleViewSet,
                basename='personsample')
urlpatterns = router.urls
