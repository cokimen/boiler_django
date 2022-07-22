from .views import (PersonViewSet, SchoolViewSet)
from rest_framework.routers import DefaultRouter
router = DefaultRouter()

# import viewset/controller

router.register('person', PersonViewSet, basename='person')
router.register('school', SchoolViewSet, basename='school')
urlpatterns = router.urls
