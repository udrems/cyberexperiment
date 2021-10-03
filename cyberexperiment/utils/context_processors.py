from django.conf import settings

from cyberexperiment.lab.models import Category


def settings_context(_request):
    """Settings available by default to the templates context."""
    # Note: we intentionally do NOT expose the entire settings
    # to prevent accidental leaking of sensitive information
    return {"DEBUG": settings.DEBUG}


def category(request):
    category_object = Category.objects.all()
    context = {"category_object": category_object}
    return context
