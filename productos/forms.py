from django import forms
from .models import Producto, Categoria

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'imagen', 'categoria']

    categoria = forms.ModelChoiceField(queryset=Categoria.objects.all(), empty_label="Seleccione una categoría")
