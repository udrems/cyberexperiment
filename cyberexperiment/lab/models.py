from core.models import General, TimeStamp
from django.conf import settings
from django.db import models

# class TimeStamp(models.Model):
#     """time stamp model for inserting created at and modified time"""

#     created_at = models.DateTimeField(auto_now_add=True)
#     modified_at = models.DateTimeField(auto_now=True)

#     class Meta:
#         abstract = True


class MembershipStatus(TimeStamp):
    name = models.CharField(max_length=12)

    def __str__(self):
        return self.name


class LabMembership(TimeStamp):
    slug = models.SlugField(max_length=100)
    membership_type = models.ForeignKey(MembershipStatus, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    payment_plan_id = models.CharField(max_length=50)

    def __str__(self):
        return self.membership_type.name


class UserMembership(TimeStamp):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    payment_customer_id = models.CharField(max_length=50)
    membership_type = models.ForeignKey(LabMembership, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class LabSubscription(TimeStamp):
    active = models.BooleanField(default=False)
    user_membership = models.ForeignKey(UserMembership, on_delete=models.CASCADE)
    payment_subcription_id = models.CharField(max_length=50)

    def __str__(self):
        return self.user_membership.user.username


class Lab(TimeStamp, General):
    """Before a user create a content, he must host a lab first"""

    users = models.ManyToManyField(settings.AUTH_USER_MODEL)

    def __init__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Lab"


class LabCourse(TimeStamp, General):
    """This enable creators create courses and experiment others can follow"""

    lab = models.ForeignKey(Lab, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Lab Content"


class Lesson(TimeStamp, General):
    """lessons will be linked to a lab course that will enable the users to create multiple lessons"""

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Lesson"


class MultiImage(TimeStamp):
    """This will enable creating multiple images on the model"""
