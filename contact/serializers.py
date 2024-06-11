from rest_framework import serializers
from .models import Contact

class ContactSerializer(serializers.ModelSerializer):
    """
    Serializer for the Contact model.
    """
    
    class Meta:
        model = Contact
        fields = ['id','name', 'subject', 'email', 'message', 'created_at']
        
    def to_representation(self, instance):
        """
        Custom representation method to return an error message
        if the user is not authenticated.
        """
        request = self.context.get('request')
        if not request.user.is_authenticated:
            return { "detail": "Authentication credentials were not provided." }
        else:
            return super().to_representation(instance)