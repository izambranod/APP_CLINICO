from django.shortcuts import render
from django.views.generic.base import TemplateView


class LoginView(TemplateView):
    template_name = "Login.html"
