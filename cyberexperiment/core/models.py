from django.db import models


class TimeStamp(models.Model):
    """timestamp"""

    class Meta:
        abstract = True


class Genera(models.Model):
    class Meta:
        abstract = True
