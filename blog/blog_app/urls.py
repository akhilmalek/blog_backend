from rest_framework.routers import DefaultRouter
from .views import BlogViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'blogs', BlogViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = router.urls