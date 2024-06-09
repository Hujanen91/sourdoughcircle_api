from rest_framework import generics, permissions
from sourdoughcircle_api.permissions import IsOwnerOrReadOnly
from posts.models import Post
from posts.serializers import PostSerializer
from followers.models import Follower
from followers.serializers import FollowerSerializer

class FollowerList(generics.ListCreateAPIView):
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
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        followed_users = Follower.objects.filter(owner=user).values_list('followed', flat=True)
        return Post.objects.filter(owner__in=followed_users) \
                           .annotate(likes_count=Count('likes', distinct=True)) \
                           .annotate(comments_count=Count('comment', distinct=True)) \
                           .order_by('-created_at')