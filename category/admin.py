from django.contrib import admin
from .models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Admin view for Category.

    Displays 'id', 'name', and 'created_at'.
    Allows searching by 'name'.
    Shows 20 items per page.
    """
    list_display = ('id', 'name', 'created_at')
    search_fields = ('name',)
    list_per_page = (20)
