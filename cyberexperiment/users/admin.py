from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from cyberexperiment.users.forms import UserChangeForm, UserCreationForm

from .models import (
    Address,
    BankAccount,
    Bitcoin,
    NotificationSetting,
    PaymentAccount,
    Privacy,
    Profile,
    UserMembership,
)

User = get_user_model()


class UserMembershipInline(admin.StackedInline):
    model = UserMembership
    can_delete = False
    verbose_name_plural = "User Membership"


class NotificationSettingInline(admin.StackedInline):
    model = NotificationSetting
    can_delete = False
    verbose_name_plural = "Notification Setting "


class PrivacyInline(admin.StackedInline):
    model = Privacy
    can_delete = False
    verbose_name_plural = "Privacy"


class AddressInline(admin.StackedInline):
    model = Address
    can_delete = False
    verbose_name_plural = "Address"


class BitcoinInline(admin.StackedInline):
    model = Bitcoin
    can_delete = False
    verbose_name_plural = "Bitcoin"


class BankAccountInline(admin.StackedInline):
    model = BankAccount
    can_delete = False
    verbose_name_plural = "Bank Account"


class PaymentAccountInline(admin.StackedInline):
    model = PaymentAccount
    can_delete = False
    verbose_name_plural = "Payment Account"


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = "Profile"
    fk_name = "user"


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    inlines = (
        ProfileInline,
        NotificationSettingInline,
        PrivacyInline,
        AddressInline,
    )

    form = UserChangeForm
    add_form = UserCreationForm
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("name", "email")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    list_display = ["username", "name", "is_superuser"]
    search_fields = ["name"]
