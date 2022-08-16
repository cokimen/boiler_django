from .views import CocaColaViewSet
from .routing import CustomReadOnlyRouter
router = CustomReadOnlyRouter(trailing_slash=True)
router.register('cocacola', CocaColaViewSet)
urlpatterns = router.urls
