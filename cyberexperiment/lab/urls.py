from django.urls import path

from .views import (
    Analytic,
    CourseDetail,
    CreateCourse,
    FeedBack,
    LiveVideo,
    Message,
    MyContent,
    Notification,
    Review,
)

app_name = "lab"
urlpatterns = [
    path("content/", CreateCourse.as_view(), name="create_course"),
    path("my_content/", MyContent.as_view(), name="my_content"),
    path("analytic/", Analytic.as_view(), name="analytic"),
    path("review/", Review.as_view(), name="review"),
    path("message/", Message.as_view(), name="message"),
    path("notification/", Notification.as_view(), name="notification"),
    path("feedback/", FeedBack.as_view(), name="feedback"),
    path("experiment/", CourseDetail.as_view(), name="course_detail"),
    path("watch_experiment/", LiveVideo.as_view(), name="watch_experiment"),
]
