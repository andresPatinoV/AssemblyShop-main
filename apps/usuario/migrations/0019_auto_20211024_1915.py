# Generated by Django 3.0.2 on 2021-10-25 00:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0018_auto_20211024_1909'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='is_staff',
            new_name='is_root',
        ),
    ]
