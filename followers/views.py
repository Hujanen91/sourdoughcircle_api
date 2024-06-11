from rest_framework import generics, permissions
from sourdoughcircle_api.permissions import IsOwnerOrReadOnly
from posts.models import Post
from posts.serializers import PostSerializer
from followers.models import Follower
from followers.serializers import FollowerSerializer

class FollowerList(generics.ListCreateAPIView):
    """
    List or create follower relationships.

    - GET: Lists all followers.
    - POST: Creates a new follower relationship.
    """
    serializer_class = FollowerSerializer
    queryset = Follower.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class FollowerDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve a follower
    No Update view, as we either follow or unfollow users
    Destroy a follower, i.e. unfollow someone if owner
    """
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Follower.objects.all()
    serializer_class = FollowerSerializer


class FollowedPostsList(generics.ListAPIView):
    """
    Lists posts from followed users.

    Requires authentication.

    - GET: Lists posts from users followed by the authenticated user.
    """
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        followed_users = Follower.objects.filter(owner=user).values_list('followed', flat=True)
        return Post.objects.filter(owner__in=followed_users).order_by('-created_at')