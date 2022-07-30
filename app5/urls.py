from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('a')
urlpatterns = router.urls
