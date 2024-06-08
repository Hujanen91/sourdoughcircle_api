from django.contrib import admin
from .models import Contact

@admin.register(Contact)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject', 'email', 'created_at')
    list_filter = ('created_at',)