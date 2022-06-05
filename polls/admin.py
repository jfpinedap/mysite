"""Polls Admin."""

# Django imports
from django.contrib import admin

# Models imports
from polls.models import Question


admin.site.register(Question)

