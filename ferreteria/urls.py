from django.urls import path
from . import views

urlpatterns = [
    # HOME
    path('', views.inicio, name='inicio'),

    # AUTH
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # FORMULARIOS (SOLO EMPLEADOS)
    path('form_producto/', views.form_producto, name='form_producto'),
    path('form_proveedor/', views.form_proveedor, name='form_proveedor'),
    path('form_categoria/', views.form_categoria, name='form_categoria'),

    # CLIENTES / VISTAS PUBLICAS
    path('buscar_producto/', views.buscar_producto, name='buscar_producto'),

    # TABLAS
    path('ver_productos/', views.ver_productos, name='ver_productos'),
    path('ver_proveedores/', views.ver_proveedores, name='ver_proveedores'),
    path('ver_categorias/', views.ver_categorias, name='ver_categorias'),

    # INFO
    path('acerca/', views.acerca, name='acerca'),
]
