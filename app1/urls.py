from rest_framework.routers import DefaultRouter
# import viewset / controller
from .views import (GameDetailViewSet, GameViewSet)

router = DefaultRouter()
router.register('game', GameViewSet, basename='game')
router.register('gamedetail', GameDetailViewSet, basename='gamedetail')
urlpatterns = router.urls
