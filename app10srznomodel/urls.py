from .views import TreeViewSet, TreeViewSetSrzNoModel
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('tree', TreeViewSet, basename='tree')
router.register('treesrznomodel', TreeViewSetSrzNoModel,
                basename='treesrznomodel')
urlpatterns = router.urls
