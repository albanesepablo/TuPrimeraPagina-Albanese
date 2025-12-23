from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import Producto, Proveedor, Categoria
from django.contrib.auth.forms import AuthenticationForm

# Página principal (base/navbar)
def index(request):
    return render(request, 'ferreteria/index.html')

# Inicio para todos
def inicio(request):
    return render(request, 'ferreteria/inicio.html')

# Login
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('inicio')
    else:
        form = AuthenticationForm()
    return render(request, 'ferreteria/login.html', {'form': form})

# Logout
def logout_view(request):
    logout(request)
    return redirect('inicio')

# Formulario de productos (solo empleados)
@login_required
def form_producto(request):
    categorias = Categoria.objects.all()
    proveedores = Proveedor.objects.all()
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        precio = request.POST.get('precio')
        categoria_id = request.POST.get('categoria')
        proveedor_id = request.POST.get('proveedor')
        categoria = Categoria.objects.get(id=categoria_id)
        proveedor = Proveedor.objects.get(id=proveedor_id)
        Producto.objects.create(nombre=nombre, precio=precio, categoria=categoria, proveedor=proveedor)
        return redirect('inicio')
    return render(request, 'ferreteria/form_producto.html', {'categorias': categorias, 'proveedores': proveedores})

# Formulario de categorías (solo empleados)
@login_required
def form_categoria(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        Categoria.objects.create(nombre=nombre)
        return redirect('inicio')
    return render(request, 'ferreteria/form_categoria.html')

# Formulario de proveedores (solo empleados)
@login_required
def form_proveedor(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        telefono = request.POST.get('telefono')
        email = request.POST.get('email')
        Proveedor.objects.create(nombre=nombre, telefono=telefono, email=email)
        return redirect('inicio')
    return render(request, 'ferreteria/form_proveedor.html')

# Ver productos
def ver_productos(request):
    productos = Producto.objects.all()
    return render(request, 'ferreteria/ver_productos.html', {'productos': productos})

# Buscar productos
def buscar_producto(request):
    productos = []
    query = request.GET.get('q')
    if query:
        productos = Producto.objects.filter(nombre__icontains=query)
    return render(request, 'ferreteria/buscar_producto.html', {'productos': productos})

# Ver proveedores
def ver_proveedores(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'ferreteria/ver_proveedores.html', {'proveedores': proveedores})

# Ver categorías
def ver_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'ferreteria/ver_categorias.html', {'categorias': categorias})

# Acerca de nosotros
def acerca(request):
    return render(request, 'ferreteria/acerca.html')
