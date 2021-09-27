from django.conf import settings
from django.db import models
from django.urls import redirect


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


class Blog(TimeStamp, General):
    excerpt = models.TextField(blank=True)
    view_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def get_absolute_url(self, *args, **kwargs):
        return redirect("core:detail", kwargs={"slug": self.slug})


class Event(TimeStamp, General):
    excerpt = models.TextField(blank=True)
    view_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def get_absolute_url(self, *args, **kwargs):
        return redirect("core:detail", kwargs={"slug": self.slug})
