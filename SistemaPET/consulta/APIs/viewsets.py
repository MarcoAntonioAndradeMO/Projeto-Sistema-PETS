from rest_framework import viewsets
from SistemaPET.consulta.APIs.serializers import ConsultaSerializer
from SistemaPET.consulta.models import Consulta


class ConsultaViewSet(viewsets.ModelViewSet):
    serializer_class = ConsultaSerializer
    queryset = Consulta.objects.all()
