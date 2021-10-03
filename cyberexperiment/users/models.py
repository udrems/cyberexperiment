from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import CharField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField

ACCOUNT_TYPE = (
    ("follower", "follower"),
    ("creators", "creators"),
)


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


# class MembershipStatus(General, TimeStamp):
#     name = models.CharField(max_length=12)
#     price = models.DecimalField(decimal_places=2, max_digits=8, default=0)

#     def __str__(self):
#         return self.name

#     class Meta:
#         verbose_name_plural = "Membership Status"

MembershipStatus = (("free", "free"), ("premium", "premium"))


class UserMembership(TimeStamp):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    membership_type = models.CharField(
        choices=MembershipStatus, default="free", max_length=20
    )

    def __str__(self):
        return self.user.username


class Profile(TimeStamp):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bio = models.TextField(
        blank=True,
        help_text="Links and coupon codes are not permitted in this section. write about yourself",
    )
    profession = models.TextField(
        blank=True,
        help_text='Add a professional headline like, "Engineer at CNC" or "Architect." I  am a Web Designer',
    )
    # social profile
    website_link = models.URLField(blank=True, default="https://")
    facebook_link = models.URLField(blank=True, default="https://facebook.com/")
    twitter_link = models.URLField(blank=True, default="https://twitter.com/")
    linkedin_link = models.URLField(blank=True, default="https://linkedin.com/")
    youtube_link = models.URLField(blank=True, default="https://youtube.com/")

    def __str__(self):
        return self.user.username


class NotificationSetting(TimeStamp):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    subscription = models.BooleanField(default=False)
    recommended_courses = models.BooleanField(default=False)
    activity_on_comment = models.BooleanField(default=False)
    replies_to_comment = models.BooleanField(default=False)
    email_notification = models.BooleanField(default=False)
    promotion_and_helpful_resources = models.BooleanField(default=False)
    announcement_from_creators = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


class Privacy(TimeStamp):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    show_profile_on_search_engine = models.BooleanField(default=False)
    show_course_you_are_taking = models.BooleanField(default=False)

    def __str__(self):
        self.user.username

    class Meta:
        verbose_name_plural = "Privacy"


class Address(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    country = CountryField()
    address_1 = models.TextField(blank=True)
    address_2 = models.TextField(blank=True)
    postcode = models.CharField(blank=True, max_length=200)
    phone = PhoneNumberField()

    def __str__(self):
        return self.user.username


class Bitcoin(TimeStamp):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    enter_wallet = models.CharField(max_length=200)
    confirm_wallet = models.CharField(max_length=200)

    def __str__(self):
        return self.user.username


class BankAccount(TimeStamp):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200)
    address = models.TextField(blank=True)
    country = CountryField()
    swift_code = models.CharField(max_length=200)
    bank_account_number = models.PositiveIntegerField(
        blank=True, help_text="check your account"
    )
    bank_name = models.CharField(
        blank=True, help_text="check your account", max_length=200
    )
    bank_address = models.CharField(
        blank=True, help_text="check your account", max_length=200
    )

    def __str__(self):
        return self.full_name


class PaymentAccount(TimeStamp):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bitcoin = models.ForeignKey(Bitcoin, on_delete=models.CASCADE)
    bank_account = models.ForeignKey(BankAccount, on_delete=models.CASCADE)

    def __str__(self):
        return self.bitcoin.user.username
