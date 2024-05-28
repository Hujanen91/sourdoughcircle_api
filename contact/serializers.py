from rest_framework import serializers
from .models import Contact

class ContactSerializer(serializers.ModelSerializer):
    
    name = serializers.ReadOnlyField(source="name.username")
    
    class Meta:
        model = Contact
        fields = ['name', 'subject', 'email', 'message']