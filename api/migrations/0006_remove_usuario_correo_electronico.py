# Generated by Django 5.0.4 on 2024-05-14 08:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_usuario_managers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='correo_electronico',
        ),
    ]