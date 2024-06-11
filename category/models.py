from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    """
    Represents a category within an application.

    Attributes:
        name (CharField): Unique category name, max length 64 chars.
        created_at (DateTimeField): Timestamp of category creation.
        updated_at (DateTimeField): Timestamp of last category update.

    Methods:
        __str__() -> str: Returns category name as string.
    """
    
    name = models.CharField(max_length=64, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name