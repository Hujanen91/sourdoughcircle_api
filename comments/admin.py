from django.contrib import admin
from .models import Comment


@admin.register(Comment)
class CommentsAdmin(admin.ModelAdmin):
    """
    Admin view for Comment.

    Displays 'owner', 'content', and 'created_at'.
    Filters by 'created_at'.
    """
    list_display = ('owner', 'content', 'created_at')
    list_filter = ('created_at',)
