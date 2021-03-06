# Generated by Django 3.0.2 on 2021-11-28 04:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tienda', '0002_producto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pc',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('comprador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('productos', models.ManyToManyField(to='tienda.Producto')),
            ],
            options={
                'verbose_name': 'PC',
                'verbose_name_plural': 'PCs',
            },
        ),
    ]
