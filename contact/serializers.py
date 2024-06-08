from rest_framework import serializers
from .models import Contact

class ContactSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Contact
        fields = ['id','name', 'subject', 'email', 'message', 'created_at']
        
    def to_representation(self, instance):
    # Access request object from serializer context
        request = self.context.get('request')
        if not request.user.is_authenticated:
        # Exclude message field for unauthenticated users
            return { "detail": "Authentication credentials were not provided." }
        else:
        # Return all fields for authenticated users
            return super().to_representation(instance)