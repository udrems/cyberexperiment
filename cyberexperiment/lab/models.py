from django.conf import settings
from django.db import models

# from cyberexperiment.users.models import UserMembership


class TimeStamp(models.Model):
    """timestamp to capture all the time of event in the database"""

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


# general model
class General(models.Model):
    """General model enable other models similar fields to be inherited. it is use to enforce dry principle"""

    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=50, unique=True)
    detail = models.TextField(blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class Category(TimeStamp, General):
    def __str__(self):
        return self.title


# class LabSubscription(TimeStamp):
#     active = models.BooleanField(default=False)
#     user_membership = models.ForeignKey(UserMembership, on_delete=models.CASCADE)
#     payment_subcription_id = models.CharField(max_length=50)

#     def __str__(self):
#         return self.user_membership.user.username


class Lab(TimeStamp, General):
    """Before a user create a content, he must host a lab first"""

    users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="lab_user")

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
