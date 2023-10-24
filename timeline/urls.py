from rest_framework.routers import DefaultRouter

from .api.views import CommentViewSet, PostViewSet, StoryViewSet

router = DefaultRouter()
router.register("posts", PostViewSet, basename="posts")
router.register("comments", CommentViewSet, basename="comments")
router.register("stories", StoryViewSet, basename="stories")

urlpatterns = router.urls
