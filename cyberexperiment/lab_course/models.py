from django.conf import settings
from django.db import models

from .lab.models import LabMembership, TimeStamp


class Team(TimeStamp):
    user = models.ManyToManyField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    description = models.TextField(max_length=5000)

    def __str__(self):
        return self.user.username


class Lab(TimeStamp):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, blank=True, null=True)
    description = models.TextField(max_length=5000)
    allowed_membership = models.ForeignKey(LabMembership, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class LabExperiment(TimeStamp):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=50)
    experiment = models.ForeignKey(Lab, on_delete=models.CASCADE)
    position = models.IntegerField(default=1)
    video = models.URLField(blank=True)
    thumbnail = models.ImageField(upload_to="lab/")

    def __str__(self):
        return self.title
