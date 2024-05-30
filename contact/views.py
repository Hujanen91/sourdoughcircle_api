from rest_framework import generics, permissions
from .models import Contact
from .serializers import ContactSerializer

class ContactList(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    

class ContactDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [permissions.IsAdminUser]
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serailizer = self.get_serializer(instance, data=request.data)
        serailizer.is_valid(raise_exception=True)
        serailizer.save()
        
        # Check for updated admin response
        if request.data.get('admin_response') and not instance.responded:
            try:
            # send admin response email back to user email
                send_email(
                    subject=request.data.get('Re:' 'subject'),
                    message=request.data.get('admin_response'),
                    from_email="sourdoughcircle@no-response.com",
                    recipient_list=[instance.email],
                    fail_silently=True,
                )
                instance.responded = True
                instance.save()
            except SuspiciousOperation as e:
                # Handle email sending error
                print(f"Error sending email: {e}")
        
        return Response(serializer.data)