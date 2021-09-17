from django.contrib import admin

from .models import LabMembership, LabSubscription, UserMembership

admin.site.register(LabMembership)
admin.site.register(UserMembership)
admin.site.register(LabSubscription)
