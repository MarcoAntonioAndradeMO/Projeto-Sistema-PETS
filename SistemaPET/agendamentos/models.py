from uuid import uuid4

from django.db import models

from SistemaPET.pacientes.models import Paciente
from SistemaPET.veterinarios.models import Veterinario


class Agendamento(models.Model):
    uuid = models.UUIDField(unique=True, primary_key=True, editable=False, default=uuid4)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, verbose_name="Nome do Paciente")
    veterinario = models.ForeignKey(Veterinario, on_delete=models.CASCADE, verbose_name="Nome do Veterinário")
    data_consulta = models.DateTimeField(verbose_name="Data da Consulta")

