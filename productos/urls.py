from django.urls import path
from . import views
from .views import pagina_principal, registro

urlpatterns = [
    path('', pagina_principal, name='pagina_principal'),
    path('lista_productos', views.lista_productos, name='lista_productos'),
    path('agregar/', views.agregar_producto, name='agregar_producto'),
    path('registro/', registro, name='registro'),
    path('producto/<int:producto_id>/agregar/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('mi-carrito/', views.mi_carrito, name='mi_carrito'),
]
