from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('producto/nuevo/', views.crear_producto, name='crear_producto'),
    path('categoria/nuevo/', views.crear_categoria, name='crear_categoria'),
    path('proveedor/nuevo/', views.crear_proveedor, name='crear_proveedor'),
    path('producto/buscar/', views.buscar_producto, name='buscar_producto'),
]
