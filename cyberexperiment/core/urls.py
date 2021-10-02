from django.urls import path

from .views import (
    AboutView,
    BlogDetailView,
    BlogView,
    ContactView,
    Dashboard,
    EventView,
    FollowerView,
    HomePageView,
    InstructorView,
)

app_name = "core"

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutView.as_view(), name="about"),
    path("blog/", BlogView.as_view(), name="blog"),
    path("contact/", ContactView.as_view(), name="contact"),
    path("blog-detail", BlogDetailView.as_view(), name="blog-details"),
    path("event/", EventView.as_view(), name="event"),
    path("follower/", FollowerView.as_view(), name="follower"),
    path("instructor/", InstructorView.as_view(), name="instructor"),
    path("dashboard/", Dashboard.as_view(), name="dashboard"),
]
