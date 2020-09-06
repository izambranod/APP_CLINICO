from django.shortcuts import render
from django.views.generic.base import TemplateView


class InicioView(TemplateView):
    template_name = "index.html"


class AtencionView(TemplateView):
    template_name = "atencion/atencion.html"



