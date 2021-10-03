from django.urls import path

from cyberexperiment.users.views import (
    CreatorDashboard,
    Profile,
    user_redirect_view,
    user_update_view,
)

app_name = "users"
urlpatterns = [
    path("~redirect/", view=user_redirect_view, name="redirect"),
    path("~update/", view=user_update_view, name="update"),
    path("profile/", Profile.as_view(), name="profile"),
    # path("<str:username>/", view=user_detail_view, name="detail"),
    path("creator_dashboard/", CreatorDashboard.as_view(), name="creator_dashboard"),
]
