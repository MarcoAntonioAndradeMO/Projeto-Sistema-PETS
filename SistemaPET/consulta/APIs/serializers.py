from rest_framework import serializers
from SistemaPET.consulta.models import Consulta


class ConsultaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consulta
        fields = '__all__'
