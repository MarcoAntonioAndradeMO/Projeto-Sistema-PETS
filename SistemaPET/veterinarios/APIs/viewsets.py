from rest_framework import viewsets
from SistemaPET.veterinarios.APIs.serializers import VeterinarioSerializer
from SistemaPET.veterinarios.models import Veterinario


class VeterinarioViewSet(viewsets.ModelViewSet):
    serializer_class = VeterinarioSerializer
    queryset = Veterinario.objects.all()
