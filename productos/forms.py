from django import forms
from .models import Producto, Categoria, Perfil , MensajeContacto
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'imagen', 'categoria', 'stock', 'sku', 'talla', 'colores', 'descuento', 'estado']

    categoria = forms.ModelChoiceField(queryset=Categoria.objects.all(), empty_label="Seleccione una categoría")

class RegistroForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean_password2(self):
        """Verifica que las contraseñas coincidan"""
        password = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")
        if password and password2 and password != password2:
            raise forms.ValidationError("Las contraseñas no coinciden")
        return password2

#formulario para editar perfil 
class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['telefono', 'direccion']

class UserForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['email']


# Formulario para editar el perfil
class PerfilForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

# Formulario para agregar dirección
class DireccionForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['direccion']
        widgets = {
            'direccion': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
        }

#formulario para enviar mensaje de contacto
# productos/forms.py

class MensajeContactoForm(forms.ModelForm):
    class Meta:
        model = MensajeContacto
        fields = ['nombre', 'email', 'mensaje']