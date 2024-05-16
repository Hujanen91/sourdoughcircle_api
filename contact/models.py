from django.db import models


class ContactForm(models.Model):
    """
    Model to handle the contact form
    submission.
    The model also handles a response field
    for the admin on the admin side so they 
    can answer members messages directly on
    the admin website.
    """
    name = models.CharField(max_length=200)
    subject = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField(max_length=700)
    read = models.BooleanField(default=False)
    admin_response = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"Message from {self.name}"