# Generated by Django 5.1.7 on 2025-03-11 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0009_producto_colores_producto_descuento_producto_estado_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='talla',
            field=models.CharField(choices=[('XS', 'XS'), ('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL')], default='XS', max_length=100),
        ),
    ]
