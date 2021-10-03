# from django.shortcuts import render
from django.views import generic


class CreateCourse(generic.TemplateView):
    template_name = "circus/create_new_course.html"


class MyContent(generic.TemplateView):
    template_name = "circus/my_contents.html"


class Analytic(generic.TemplateView):
    template_name = "circus/analytic.html"


class Message(generic.TemplateView):
    template_name = "circus/messages.html"


class Notification(generic.TemplateView):
    template_name = "circus/notification.html"


class Review(generic.TemplateView):
    template_name = "circus/review.html"


class FeedBack(generic.TemplateView):
    template_name = "circus/feedback.html"
