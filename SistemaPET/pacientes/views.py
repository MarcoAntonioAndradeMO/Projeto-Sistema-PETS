from django.shortcuts import render
from django.views.generic import TemplateView


class PacientesView(TemplateView):
    template_name = 'pacientes.html'


class PaginaPacienteView(TemplateView):
    template_name = 'pagina_paciente.html'

    def get_context_data(self, **kwargs):
        context = super(PaginaPacienteView, self).get_context_data()
        context['cpf'] = kwargs['cpf']
        return context


class ConsultarPacienteView(TemplateView):
    template_name = 'consulta_paciente.html'

