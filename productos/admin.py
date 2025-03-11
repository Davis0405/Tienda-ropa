from django.contrib import admin
from .models import Producto, Categoria, MensajeContacto

admin.site.register(Producto)
admin.site.register(Categoria)
admin.site.register(MensajeContacto)