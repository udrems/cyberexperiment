from django.urls import path

from .views import CreateCourse

app_name = "lab"
urlpatterns = [
    path("content/", CreateCourse.as_view(), name="create_course"),
]
