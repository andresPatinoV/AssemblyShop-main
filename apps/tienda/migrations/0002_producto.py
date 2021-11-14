# Generated by Django 3.0.2 on 2021-11-14 21:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('descripcion', models.TextField(blank=True, null=True, verbose_name='Descripcion')),
                ('precio', models.FloatField(verbose_name='Precio')),
                ('cantidad', models.SmallIntegerField(default=1, verbose_name='Cantidad')),
                ('imagen', models.ImageField(blank=True, max_length=255, null=True, upload_to='productos/', verbose_name='Imagen')),
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha Creacion')),
                ('fecha_actualizacion', models.DateField(auto_now=True, verbose_name='Fecha Actualizacion')),
                ('categoria_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tienda.Categoria')),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
            },
        ),
    ]
