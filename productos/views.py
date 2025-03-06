from django.shortcuts import render, redirect
from .models import Producto, Categoria, Carrito, CarritoProducto
from .forms import ProductoForm, RegistroForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required


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
    
    return render(request, 'carrito.html', {'productos_carrito': productos_carrito})

@login_required
def mi_carrito(request):
    carrito = Carrito.objects.get(user=request.user)
    productos_carrito = CarritoProducto.objects.filter(carrito=carrito)
    total = sum(item.producto.precio * item.cantidad for item in productos_carrito)
    
    return render(request, 'carrito.html', {'productos_carrito': productos_carrito, 'total': total})

@login_required
def eliminar_del_carrito(request, carrito_producto_id):
    carrito_producto = CarritoProducto.objects.get(id=carrito_producto_id)
    carrito_producto.delete()
    
    return redirect('mi_carrito')