from uuid import uuid4

from django.db import models

from SistemaPET.agendamentos.models import Agendamento


class Consulta(models.Model):
    uuid = models.UUIDField(unique=True, primary_key=True, editable=False, default=uuid4)
    agendamento = models.ForeignKey(Agendamento, on_delete=models.CASCADE, verbose_name="Agendamento")
    receituario = models.CharField(max_length=200, verbose_name="Receituário")
    exame = models.CharField(max_length=200, verbose_name="Exames")
