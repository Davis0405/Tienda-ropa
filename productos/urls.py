from django.urls import path
from . import views
from .views import pagina_principal 

urlpatterns = [
    path('', pagina_principal, name='pagina_principal'),
    path('lista_productos', views.lista_productos, name='lista_productos'),
    path('agregar/', views.agregar_producto, name='agregar_producto'),
]
