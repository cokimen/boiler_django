from .views import BookViewSet, BookOtViewSet
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('book', BookViewSet, basename='book')
router.register('bookot', BookOtViewSet, basename='bookot')
urlpatterns = router.urls
