# Generated by Django 3.0.2 on 2021-10-18 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0004_auto_20211018_1746'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='username',
            field=models.CharField(default=None, max_length=200, verbose_name='Nombre de usuario'),
            preserve_default=False,
        ),
    ]
