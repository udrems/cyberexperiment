import stripe
from django.conf import settings
from django.db.models.signal import post_save

from .models import UserMembership


def post_save_create_usermembership(sender, instance, created, *args, **kwargs):
    if created:
        UserMembership.objects.get_or_create(user=instance)
    user_membership = UserMembership.objects.get_or_create(user=instance)
    if (
        user_membership.payment_customer_id is None
        or user_membership.payment_customer_id == " "
    ):
        new_customer_id = stripe.Customer.create(email=instance.email)
        user_membership.payment_customer_id = new_customer_id["id"]
        user_membership.save()


post_save.connect(post_save_create_usermembership, sender=settings.AUTH_USER_MODEL)
