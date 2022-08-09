from .views import HandphoneViewSet
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('handphone', HandphoneViewSet, basename='handphone')
urlpatterns = router.urls
