from django.contrib import admin
from .models import Producto, Categoria, MensajeContacto, Perfil, Carrito, CarritoProducto

admin.site.register(Producto)
admin.site.register(Categoria)
admin.site.register(MensajeContacto)
admin.site.register(Perfil)
admin.site.register(Carrito)
admin.site.register(CarritoProducto)