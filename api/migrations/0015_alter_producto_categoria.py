# Generated by Django 5.0.4 on 2024-05-31 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_alter_producto_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='categoria',
            field=models.CharField(choices=[('ordenadores', 'Ordenadores'), ('portatiles', 'Portátiles'), ('moviles', 'Moviles'), ('perifericos', 'Periféricos'), ('componentes', 'Componentes'), ('accesorios', 'Accesorios')], max_length=50),
        ),
    ]
