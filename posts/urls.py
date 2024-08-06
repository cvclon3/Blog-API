from rest_framework import routers

from .views import PostViewSet, UserViewSet


router = routers.SimpleRouter()
router.register('users', UserViewSet, basename='users')
router.register('', PostViewSet, basename='posts')

urlpatterns = router.urls
