from django.shortcuts import render
from django.views.generic import TemplateView

from SistemaPET.pacientes.models import Paciente
from SistemaPET.veterinarios.models import Veterinario


class AgendamentoView(TemplateView):
    template_name = 'agendamento.html'

    def get_context_data(self, **kwargs):
        context = super(AgendamentoView, self).get_context_data()
        context['pacientes'] = Paciente.objects.all()
        context['veterinarios'] = Veterinario.objects.all()
        return context

