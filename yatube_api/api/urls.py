from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, GroupViewSet, CommentViewSet
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post-api')
router.register(r'groups', GroupViewSet, basename='group-api')
router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comment-api'
)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/api-token-auth/', obtain_auth_token),
]
