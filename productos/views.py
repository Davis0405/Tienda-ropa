from django.shortcuts import render
from .models import Producto

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos/lista_productos.html', {'productos': productos})

from django.shortcuts import render, redirect
from .forms import ProductoForm
from .models import Categoria

def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')  # Redirige a una página que muestra el producto agregado
    else:
        form = ProductoForm()
    return render(request, 'productos/agregar_producto.html', {'form': form})

