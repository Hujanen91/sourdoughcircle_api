from django.contrib import admin
from .models import Contact

@admin.register(Contact)
class ContactsAdmin(admin.ModelAdmin):
    """
    Admin view for Contact.

    Displays 'name', 'subject', 'email', and 'created_at'.
    Filters by 'created_at'.
    """
    list_display = ('name', 'subject', 'email', 'created_at')
    list_filter = ('created_at',)