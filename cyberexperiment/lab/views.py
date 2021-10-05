# from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic


class CreateCourse(LoginRequiredMixin, generic.TemplateView):
    template_name = "circus/create_new_course.html"


class MyContent(LoginRequiredMixin, generic.TemplateView):
    template_name = "circus/my_contents.html"


class Analytic(LoginRequiredMixin, generic.TemplateView):
    template_name = "circus/analytic.html"


class Message(LoginRequiredMixin, generic.TemplateView):
    template_name = "circus/messages.html"


class Notification(LoginRequiredMixin, generic.TemplateView):
    template_name = "circus/notification.html"


class Review(LoginRequiredMixin, generic.TemplateView):
    template_name = "circus/review.html"


class FeedBack(LoginRequiredMixin, generic.TemplateView):
    template_name = "circus/feedback.html"


class CourseDetail(LoginRequiredMixin, generic.TemplateView):
    template_name = "circus/course_detail_view.html"


class LiveVideo(LoginRequiredMixin, generic.TemplateView):
    template_name = "circus/live_output.html"


class AllCreator(LoginRequiredMixin, generic.TemplateView):
    template_name = "circus/all_instructor.html"


class Explore(LoginRequiredMixin, generic.TemplateView):
    template_name = "circus/explore.html"


class Membership(LoginRequiredMixin, generic.TemplateView):
    template_name = "circus/membership.html"


class Checkout(LoginRequiredMixin, generic.TemplateView):
    template_name = "circus/checkout_membership.html"
