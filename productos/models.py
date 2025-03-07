from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to='productos/')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='productos', null=True, blank=True)


    def __str__(self):
        return self.nombre

class Carrito(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    productos = models.ManyToManyField(Producto, through='CarritoProducto')
    
    def __str__(self):
        return f"Carrito de {self.user.username}"
    
class CarritoProducto(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)

from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
    direccion = models.TextField(blank=True, null=True, default="")
    telefono = models.CharField(max_length=20, blank=True, null=True, default="")
    fecha_creacion = models.DateTimeField(default=timezone.now)    # Guarda la fecha en que se creó el perfil
    updated_at = models.DateTimeField(auto_now=True)  # Guarda la fecha de la última actualización

    def __str__(self):
        return f'Perfil de {self.user.username}'

    def get_direccion(self):
        return self.direccion if self.direccion else "Sin dirección registrada"
