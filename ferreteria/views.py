from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Producto, Proveedor, Categoria


# =========================
# VISTAS GENERALES
# =========================

def inicio(request):
    return render(request, 'ferreteria/inicio.html')


def login_view(request):
    if request.method == 'POST':
        user = authenticate(
            request,
            username=request.POST.get('username'),
            password=request.POST.get('password')
        )
        if user is not None:
            login(request, user)
            return redirect('inicio')
    return render(request, 'ferreteria/login.html')


def logout_view(request):
    logout(request)
    return redirect('inicio')


# =========================
# FORMULARIOS (SOLO EMPLEADOS)
# =========================

@login_required
def form_producto(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        precio = request.POST.get('precio')
        categoria = request.POST.get('categoria')
        proveedor = request.POST.get('proveedor')

        Producto.objects.create(
            nombre=nombre,
            precio=precio,
            categoria=categoria,
            proveedor=proveedor
        )
        return redirect('ver_productos')

    return render(request, 'ferreteria/form_producto.html')


@login_required
def form_proveedor(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        telefono = request.POST.get('telefono')
        email = request.POST.get('email')

        Proveedor.objects.create(
            nombre=nombre,
            telefono=telefono,
            email=email
        )
        return redirect('ver_proveedores')

    return render(request, 'ferreteria/form_proveedor.html')


@login_required
def form_categoria(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')

        Categoria.objects.create(nombre=nombre)
        return redirect('ver_categorias')

    return render(request, 'ferreteria/form_categoria.html')


# =========================
# CLIENTES / VISTAS PUBLICAS
# =========================

def buscar_producto(request):
    productos = []
    query = request.GET.get('q')

    if query:
        productos = Producto.objects.filter(nombre__icontains=query)

    return render(
        request,
        'ferreteria/buscar_producto.html',
        {'productos': productos}
    )


def ver_productos(request):
    productos = Producto.objects.all()
    return render(
        request,
        'ferreteria/ver_productos.html',
        {'productos': productos}
    )


def ver_proveedores(request):
    proveedores = Proveedor.objects.all()
    return render(
        request,
        'ferreteria/ver_proveedores.html',
        {'proveedores': proveedores}
    )


def ver_categorias(request):
    categorias = Categoria.objects.all()
    return render(
        request,
        'ferreteria/ver_categorias.html',
        {'categorias': categorias}
    )


def acerca(request):
    return render(request, 'ferreteria/acerca.html')
