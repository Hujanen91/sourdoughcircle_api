from rest_framework import generics, permissions
from .models import Tags
from .serializers import TagsSerializer


class TagsList(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]