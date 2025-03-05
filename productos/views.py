from django.shortcuts import render
from .models import Producto, Categoria

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

