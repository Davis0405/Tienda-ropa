from django.urls import path
from . import views
from .views import pagina_principal, registro
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', pagina_principal, name='pagina_principal'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('lista_productos', views.lista_productos, name='lista_productos'),
    path('agregar/', views.agregar_producto, name='agregar_producto'),
    path('registro/', registro, name='registro'),
    path('producto/<int:producto_id>/agregar/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('mi-carrito/', views.mi_carrito, name='mi_carrito'),
    path('eliminar/<int:producto_id>/', views.eliminar_del_carrito, name='eliminar_del_carrito'),
    path('perfil/', views.perfil, name='perfil'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
]
