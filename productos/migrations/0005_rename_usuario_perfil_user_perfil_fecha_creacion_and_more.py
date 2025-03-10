# Generated by Django 5.0.7 on 2025-03-07 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0004_perfil'),
    ]

    operations = [
        migrations.RenameField(
            model_name='perfil',
            old_name='usuario',
            new_name='user',
        ),
        migrations.AddField(
            model_name='perfil',
            name='fecha_creacion',
            field=models.DateTimeField(auto_now_add=True, default='2024-03-05 12:00:00'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='perfil',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='direccion',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='telefono',
            field=models.CharField(blank=True, default='', max_length=20, null=True),
        ),
    ]
