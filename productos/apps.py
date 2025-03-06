from django.apps import AppConfig


class ProductosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'productos'

# apps.py
from django.apps import AppConfig

class TuAplicacionConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tu_aplicacion'

    def ready(self):
        import productos.signals  # Asegúrate de que se registre la señal

