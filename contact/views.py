from rest_framework import generics, permissions
from .models import Contact
from .serializers import ContactSerializer

class ContactList(generics.ListCreateAPIView):
    """
    API view to list or create contacts.

    - GET: Lists all contacts.
    - POST: Creates a new contact.
    """
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [permissions.AllowAny]
    

class ContactDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update, or delete a contact by id.

    - GET: Retrieves a contact.
    - PUT: Updates a contact.
    - DELETE: Deletes a contact.
    """
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [permissions.IsAuthenticated]