# Generated by Django 4.2a1 on 2023-02-04 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("consulta", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="consulta",
            name="exame",
            field=models.CharField(max_length=200, verbose_name="Exames"),
        ),
    ]