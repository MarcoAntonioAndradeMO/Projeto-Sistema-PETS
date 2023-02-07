from uuid import uuid4

from django.db import models


class Veterinario(models.Model):
    uuid = models.UUIDField(unique=True, primary_key=True, editable=False, default=uuid4)
    cmrv = models.CharField(max_length=15)
    nome = models.CharField(max_length=200)
    especialidade = models.CharField(max_length=50)

    def __str__(self):
        return str(f'{self.nome}')
