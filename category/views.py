from rest_framework import generics, permissions
from .models import Category
from .serializers import CategorySerializer, CategoryDetailSerializer
from sourdoughcircle_api.permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend

class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']
    
    
class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a category, or update or delete it by id if you own it.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = CategoryDetailSerializer
    queryset = Category.objects.all()