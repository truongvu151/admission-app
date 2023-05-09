from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import UserAccount, UserProfile

# create and save user profile
@receiver(post_save, sender = UserAccount)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user = instance)

@receiver(post_save, sender = UserAccount)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()