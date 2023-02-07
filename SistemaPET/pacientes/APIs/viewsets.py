from rest_framework import viewsets
from SistemaPET.pacientes.APIs.serializers import PacienteSerializer
from SistemaPET.pacientes.models import Paciente


class PacienteViewSet(viewsets.ModelViewSet):
    serializer_class = PacienteSerializer
    queryset = Paciente.objects.all()

    def get_queryset(self):
        queryset = self.queryset.all()
        cpf = self.request.query_params.get("cpf")
        if cpf:
            queryset = queryset.filter(cpf=cpf)
        return queryset
