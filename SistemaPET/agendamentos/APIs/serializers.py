from rest_framework import serializers
from SistemaPET.agendamentos.models import Agendamento
from SistemaPET.pacientes.APIs.serializers import PacienteSerializer
from SistemaPET.veterinarios.APIs.serializers import VeterinarioSerializer


class AgendamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agendamento
        fields = '__all__'


class ListAgendamentoSerializer(serializers.ModelSerializer):
    paciente = PacienteSerializer()
    veterinario = VeterinarioSerializer()

    class Meta:
        model = Agendamento
        fields = '__all__'
