# Generated by Django 3.0.2 on 2021-10-18 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0005_usuario_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='username',
            field=models.CharField(max_length=200, null=True, verbose_name='Nombre de usuario'),
        ),
    ]
