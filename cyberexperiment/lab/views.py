# from django.shortcuts import render
from django.views import generic


class CreateCourse(generic.TemplateView):
    template_name = "circus/create_new_course.html"
