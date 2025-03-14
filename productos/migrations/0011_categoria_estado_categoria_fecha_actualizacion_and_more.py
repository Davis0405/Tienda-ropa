# Generated by Django 5.1.7 on 2025-03-11 20:11

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0010_alter_producto_talla'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='estado',
            field=models.CharField(choices=[('activa', 'Activa'), ('inactiva', 'Inactiva')], default='activa', max_length=50),
        ),
        migrations.AddField(
            model_name='categoria',
            name='fecha_actualizacion',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='categoria',
            name='fecha_creacion',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
