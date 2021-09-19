from django.urls import path

from .views import (
    AboutView,
    BlogDetailView,
    BlogView,
    ContactView,
    EventView,
    FollowerView,
    HomePageView,
    InstructorView,
    LoginView,
    RegisterView,
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
    path("login/", LoginView.as_view(), name="login"),
    path("register", RegisterView.as_view(), name="register"),
]
