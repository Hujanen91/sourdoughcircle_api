from rest_framework import generics, permissions
from .models import Category
from .serializers import CategorySerializer
from sourdoughcircle_api.permissions import IsOwnerOrReadOnly


class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a category, or update or delete it by id if you own it.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()