# Generated by Django 4.2a1 on 2023-02-04 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("veterinarios", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="veterinario",
            name="cmrv",
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name="veterinario",
            name="especialidade",
            field=models.CharField(max_length=50),
        ),
    ]
