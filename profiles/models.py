from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    User profile model.

    Attributes:
        owner (OneToOneField): Associated user.
        created_at (DateTimeField): Date and time of creation.
        updated_at (DateTimeField): Date and time of last update.
        name (CharField): User's name.
        email (EmailField): User's email address.
        content (TextField): Additional user information.
        image (ImageField): User's profile image.
        facebook_link (URLField): User's Facebook profile link.
        twitter_link (URLField): User's Twitter profile link.
        linkedin_link (URLField): User's LinkedIn profile link.
    """
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255, blank=True)
    email = models.EmailField(max_length=50, blank=True)
    content = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../user_6_shlqba'
    )
    facebook_link = models.URLField(blank=True)
    twitter_link = models.URLField(blank=True)
    linkedin_link = models.URLField(blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.owner}'s profile"


def create_profile(sender, instance, created, **kwargs):
    """
    Signal handler to create a profile for a new user.
    """
    if created:
        Profile.objects.create(owner=instance)


post_save.connect(create_profile, sender=User)
