from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import CharField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

ACCOUNT_TYPE = (
    ("follower", "follower"),
    ("creators", "creators"),
)


class User(AbstractUser):
    """Default user for cyberexperiment."""

    #: First and last name do not cover name patterns around the globe
    name = CharField(_("Name of User"), blank=True, max_length=255)
    first_name = models.CharField(max_length=255, blank=True)  # type: ignore
    last_name = models.CharField(max_length=255, blank=True)  # type: ignore
    account_type = models.CharField(
        max_length=255, choices=ACCOUNT_TYPE, default="follower"
    )

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})
