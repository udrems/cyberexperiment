from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Address, NotificationSetting, Privacy, Profile

user = settings.AUTH_USER_MODEL


@receiver(post_save, sender=user)
def create_user_profile(sender, created, instance, *args, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        NotificationSetting.objects.create(user=instance)
        Privacy.objects.create(user=instance)
        Address.objects.create(user=instance)
    instance.profile.save()
    instance.notificationsetting.save()
    instance.privacy.save()
    instance.address.save()
