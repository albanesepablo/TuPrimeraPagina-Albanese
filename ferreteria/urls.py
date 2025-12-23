from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('buscar-producto/', views.buscar_producto, name='buscar_producto'),
    path('crear-producto/', views.crear_producto, name='crear_producto'),
    path('crear-categoria/', views.crear_categoria, name='crear_categoria'),
    path('crear-proveedor/', views.crear_proveedor, name='crear_proveedor'),
]
