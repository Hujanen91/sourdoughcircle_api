from rest_framework import serializers
from .models import Category

class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = ['id', 'name', 'created_at']
        
class CategoryDetailSerializer(CategorySerializer):
    """
    Serializer for the Comment model used in Detail view
    Post is a read only field so that we dont have to set it on each update
    """
    name = serializers.ReadOnlyField(source='category.id')