# Generated by Django 3.0.2 on 2021-12-13 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0009_auto_20211212_2201'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='solicitud',
            name='solicitante_noregistrado',
        ),
        migrations.AlterField(
            model_name='solicitud',
            name='solicitante',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Nombre'),
        ),
    ]
