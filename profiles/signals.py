from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from django.dispatch import receiver

from profiles.models import ClientProfile


user_model = get_user_model()

@receiver(post_save, sender=user_model)
def create_profile(sender, instance, created, **kwargs):
    if created:
        ClientProfile.objects.create(user=instance)

