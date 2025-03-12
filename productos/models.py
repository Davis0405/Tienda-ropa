from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

#----------------------------------------------------| MODELOS |----------------------------------------------------#
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(default=timezone.now)  # Valor predeterminado
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    estado = models.CharField(max_length=50, choices=[('activa', 'Activa'), ('inactiva', 'Inactiva')], default='activa')

    def __str__(self):
        return self.nombre
#----------------------------------------------------| MODELOS |----------------------------------------------------#
class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to='productos/')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='productos', null=True, blank=True)
    stock = models.PositiveIntegerField(default=0)
    fecha_creacion = models.DateTimeField(default=timezone.now)  # Valor predeterminado
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    sku = models.CharField(max_length=100, unique=True, default="No especificado")  # Valor predeterminado
    talla = models.CharField(max_length=100, choices = [('XS', 'XS'),('S', 'S'),('M', 'M'),('L', 'L'),('XL', 'XL'),], default="XS")
  # Ejemplo: "S,M,L,XL"
    colores = models.CharField(max_length=100, default="No especificado")  # Valor predeterminado
    descuento = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    estado = models.CharField(max_length=50, choices=[('disponible', 'Disponible'), ('agotado', 'Agotado')], default='disponible')
#----------------------------------------------------| MODELOS |----------------------------------------------------#
    def __str__(self):
        return self.nombre


    def __str__(self):
        return self.nombre
#----------------------------------------------------| MODELOS |----------------------------------------------------#
class Carrito(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    productos = models.ManyToManyField(Producto, through='CarritoProducto')
    fecha_creacion = models.DateTimeField(default=timezone.now)  # Valor predeterminado
    estado = models.CharField(max_length=50, choices=[('activo', 'Activo'), ('completado', 'Completado'), ('cancelado', 'Cancelado')], default='activo')
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # Nuevo campo
    confirmado = models.BooleanField(default=False)  # Nuevo campo
    
    def actualizar_total(self):
        total = sum(item.producto.precio * item.cantidad for item in self.carritoproducto_set.all())
        self.total = total
        self.save()

    def __str__(self):
        return f"Carrito de {self.user.username}"
    
class CarritoProducto(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)
    precio_total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def calcular_precio_total(self):
        self.precio_total = self.cantidad * self.producto.precio

    def save(self, *args, **kwargs):
        self.calcular_precio_total()
        super().save(*args, **kwargs)
        self.carrito.actualizar_total()  # Actualiza el total del carrito

    def __str__(self):
        return f"{self.cantidad} x {self.producto.nombre} en {self.carrito}"
    
#----------------------------------------------------| MODELOS |----------------------------------------------------#
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
    
#----------------------------------------------------| MODELOS |----------------------------------------------------#
class MensajeContacto(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    mensaje = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Mensaje de {self.nombre} - {self.email}"
