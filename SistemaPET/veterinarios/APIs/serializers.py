from rest_framework import serializers
from SistemaPET.veterinarios.models import Veterinario


class VeterinarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Veterinario
        fields = '__all__'
