from rest_framework import viewsets
from SistemaPET.agendamentos.APIs.serializers import AgendamentoSerializer, ListAgendamentoSerializer
from SistemaPET.agendamentos.models import Agendamento


class AgendamentoViewSet(viewsets.ModelViewSet):
    serializer_class = AgendamentoSerializer
    queryset = Agendamento.objects.all()

    def get_queryset(self):
        queryset = self.queryset.all()
        paciente = self.request.query_params.get("paciente")
        if paciente:
            queryset = queryset.filter(paciente__cpf=paciente)
        return queryset

    def list(self, request, *args, **kwargs):
        self.serializer_class = ListAgendamentoSerializer
        return super(AgendamentoViewSet, self).list(request, *args, **kwargs)
