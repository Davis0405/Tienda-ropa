from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, Categoria, Carrito, CarritoProducto, Perfil
from .forms import ProductoForm, RegistroForm, PerfilForm, UserForm, PerfilForm, DireccionForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse


def lista_productos(request):
    # Obtener todas las categorías
    categorias = Categoria.objects.all()
    
    # Obtener la categoría seleccionada (si hay alguna)
    categoria_id = request.GET.get('categoria')
    
    if categoria_id:
        productos = Producto.objects.filter(categoria_id=categoria_id)
    else:
        productos = Producto.objects.all()

    return render(request, 'productos/lista_productos.html', {
        'productos': productos,
        'categorias': categorias,
        'selected_categoria': categoria_id
    })
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')  # Redirige a una página que muestra el producto agregado
    else:
        form = ProductoForm()
    return render(request, 'productos/agregar_producto.html', {'form': form})
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------|

def pagina_principal(request):
    return render(request, 'productos/index.html')

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.set_password(form.cleaned_data['password'])
            usuario.save()
            login(request, usuario)  # Autenticamos al usuario después del registro
            return redirect('lista_productos')  # Redirigir a la página principal
    else:
        form = RegistroForm()
    return render(request, 'productos/registro.html', {'form': form})
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
#logica de carrito
@login_required
def agregar_al_carrito(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    carrito, created = Carrito.objects.get_or_create(user=request.user)
    
    # Verificar si el producto ya está en el carrito
    carrito_producto, created = CarritoProducto.objects.get_or_create(carrito=carrito, producto=producto)
    if not created:
        carrito_producto.cantidad += 1  # Si ya está, incrementamos la cantidad
        carrito_producto.save()

    return redirect('mi_carrito')  # Redirige a la página del carrito
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------|

@login_required
def mi_carrito(request):
    carrito = Carrito.objects.get(user=request.user)
    productos_carrito = CarritoProducto.objects.filter(carrito=carrito)
    
    # Calcula el total
    total = 0
    for item in productos_carrito:
        total += item.producto.precio * item.cantidad
    
    return render(request, 'productos/carrito.html', {'productos_carrito': productos_carrito, 'total': total})

@login_required
def eliminar_del_carrito(request, producto_id):
    # Obtén el objeto relacionado con el producto
    carrito_producto = get_object_or_404(CarritoProducto, id=producto_id)
    
    # Elimina el producto del carrito
    carrito_producto.delete()

    # Redirige a la página del carrito o a donde desees
    return redirect('mi_carrito')

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
@login_required
def perfil(request):
    try:
        perfil = Perfil.objects.get(usuario=request.user)
    except Perfil.DoesNotExist:
        perfil = None
    
    if request.method == 'POST':
        if perfil:
            form = PerfilForm(request.POST, instance=perfil)
        else:
            form = PerfilForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('perfil')  # Redirige al perfil actualizado

    else:
        if perfil:
            form = PerfilForm(instance=perfil)
        else:
            form = PerfilForm()
    
    return render(request, 'productos/perfil.html', {'form': form})

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
@login_required
def editar_perfil(request):
    if request.method == "POST":
        form = PerfilForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('perfil')  # Redirigir al perfil después de editar
    else:
        form = PerfilForm(instance=request.user)

    return render(request, 'productos/editar_perfil.html', {'form': form})

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
@login_required
def agregar_direccion(request):
    perfil, created = Perfil.objects.get_or_create(usuario=request.user)

    if request.method == "POST":
        form = DireccionForm(request.POST, instance=perfil)
        if form.is_valid():
            form.save()
            return redirect('perfil')

    else:
        form = DireccionForm(instance=perfil)

    return render(request, 'productos/agregar_direccion.html', {'form': form})

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
#vista para el modal de list_productos
def obtener_detalle_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    data = {
        "nombre": producto.nombre,
        "descripcion": producto.descripcion,
        "precio": producto.precio,
        "imagen": producto.imagen.url,
        "categoria": producto.categoria.nombre
    }
    return JsonResponse(data)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
#vista para contactar
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from .models import MensajeContacto  # Asegúrate de crear este modelo
from django.conf import settings

# productos/views.py

from django.shortcuts import render, redirect
from .forms import MensajeContacto

# productos/views.py

from django.shortcuts import render, redirect
from .forms import MensajeContactoForm
from .models import MensajeContacto

def contacto(request):
    informacion_contacto = {
        'correo': 'contacto@tiendaropa.com',
        'telefono': '+502 1234 5678',
        'facebook': 'https://facebook.com/tiendaropa',
        'instagram': 'https://instagram.com/tiendaropa',
        'direccion': '123 Calle Principal, Ciudad, País',
    }

    if request.method == 'POST':
        form = MensajeContactoForm(request.POST)
        if form.is_valid():
            # Guarda el mensaje en la base de datos
            form.save()
            return redirect('contacto')  # Redirige a la misma página después de enviar el mensaje
    else:
        form = MensajeContactoForm()

    return render(request, 'productos/contacto.html', {
        'contacto': informacion_contacto,
        'form': form,
    })