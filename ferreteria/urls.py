from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('index/', views.index, name='index'),
    path('login/', views.login_view, name='login_view'),
    path('logout/', views.logout_view, name='logout_view'),
    path('productos/', views.ver_productos, name='ver_productos'),
    path('buscar/', views.buscar_producto, name='buscar_producto'),
    path('acerca/', views.acerca, name='acerca'),
    path('form_producto/', views.form_producto, name='form_producto'),
    path('form_categoria/', views.form_categoria, name='form_categoria'),
    path('form_proveedor/', views.form_proveedor, name='form_proveedor'),
    path('proveedores/', views.ver_proveedores, name='ver_proveedores'),
    path('categorias/', views.ver_categorias, name='ver_categorias'),
    path("detalle_producto/<int:pk>/", views.detalle_producto, name="detalle_producto"),
    path("producto/editar/<int:pk>/", views.editar_producto, name="editar_producto"),
    path("eliminar_producto/<int:pk>/", views.eliminar_producto, name="eliminar_producto"),
]
