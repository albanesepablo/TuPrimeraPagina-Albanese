from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('inicio/', views.inicio, name='inicio'),

    # Login / Logout usando Django
    path('login/', auth_views.LoginView.as_view(template_name='ferreteria/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='index'), name='logout'),

    # Formularios (solo para empleados logueados)
    path('form_producto/', views.form_producto, name='form_producto'),
    path('form_categoria/', views.form_categoria, name='form_categoria'),
    path('form_proveedor/', views.form_proveedor, name='form_proveedor'),

    # Vistas de tablas
    path('ver_productos/', views.ver_productos, name='ver_productos'),
    path('ver_proveedores/', views.ver_proveedores, name='ver_proveedores'),
    path('ver_categorias/', views.ver_categorias, name='ver_categorias'),

    # Buscar productos
    path('buscar_producto/', views.buscar_producto, name='buscar_producto'),

    # Acerca de
    path('acerca/', views.acerca, name='acerca'),
]
