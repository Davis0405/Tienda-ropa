# Generated by Django 5.1.7 on 2025-03-11 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0013_carrito_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='carrito',
            name='confirmado',
            field=models.BooleanField(default=False),
        ),
    ]
