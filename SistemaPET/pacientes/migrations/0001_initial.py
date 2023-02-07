# Generated by Django 4.2a1 on 2023-02-04 21:02

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Paciente",
            fields=[
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("cpf", models.CharField(max_length=10)),
                ("nome_do_Dono", models.CharField(max_length=50)),
                ("nome_do_Animal", models.CharField(max_length=30)),
            ],
        ),
    ]