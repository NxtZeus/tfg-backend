# Generated by Django 5.0.4 on 2024-05-31 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_alter_producto_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='categoria',
            field=models.CharField(choices=[('Ordenadores', 'ordenadores'), ('Portátiles', 'portatiles'), ('Moviles', 'moviles'), ('Periféricos', 'perifericos'), ('Componentes', 'componentes'), ('Accesorios', 'accesorios')], max_length=50),
        ),
    ]
