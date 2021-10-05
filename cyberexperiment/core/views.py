from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "core/index.html"


class AboutView(TemplateView):
    template_name = "core/about.html"


class BlogView(TemplateView):
    template_name = "core/blog.html"


class ContactView(TemplateView):
    template_name = "core/contact.html"


class BlogDetailView(TemplateView):
    template_name = "core/blog-detail.html"


class EventView(TemplateView):
    template_name = "core/events.html"


class FollowerView(TemplateView):
    template_name = "core/follower.html"


class InstructorView(TemplateView):
    template_name = "core/instructor.html"


class Dashboard(LoginRequiredMixin, TemplateView):
    template_name = "circus/index.html"
