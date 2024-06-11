from django.db import models
from django.contrib.auth.models import User


class Follower(models.Model):
    """
    Represents a follower relationship between users.

    Attributes:
        owner (ForeignKey): The user following another user.
        followed (ForeignKey): The user being followed.
        created_at (DateTimeField): Date and time of creation.
    """
    owner = models.ForeignKey(
        User, related_name='following', on_delete=models.CASCADE
    )
    followed = models.ForeignKey(
        User, related_name='followed', on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'followed']

    def __str__(self):
        return f'{self.owner} {self.followed}'
