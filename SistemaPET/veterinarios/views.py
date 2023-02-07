from django.shortcuts import render
from django.views.generic import TemplateView


class VeterinariosView(TemplateView):
    template_name = 'veterinarios.html'

