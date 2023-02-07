from uuid import uuid4

from django.db import models


class Paciente(models.Model):
    uuid = models.UUIDField(unique=True, primary_key=True, editable=False, default=uuid4)
    cpf = models.CharField(max_length=11)
    nome_do_dono = models.CharField(max_length=100)
    nome_do_animal = models.CharField(max_length=50)

    def __str__(self):
        return str(f'{self.nome_do_dono}')
