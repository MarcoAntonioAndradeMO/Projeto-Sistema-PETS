from rest_framework import serializers
from SistemaPET.pacientes.models import Paciente


class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = '__all__'
