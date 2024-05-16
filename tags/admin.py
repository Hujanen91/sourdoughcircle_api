from django.contrib import admin
from .models import Tags

@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name')
    # Set the number of items displayed per page in the admin list view
    list_per_page = (20)