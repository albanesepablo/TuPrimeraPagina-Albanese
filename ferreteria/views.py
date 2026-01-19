from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from .models import Producto, Proveedor, Categoria
from .forms import ProductoForm, CategoriaForm, ProveedorForm


def index(request):
    return render(request, 'ferreteria/index.html')


def inicio(request):
    return render(request, 'ferreteria/inicio.html')


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


def logout_view(request):
    logout(request)
    return redirect('inicio')


@login_required
def form_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = ProductoForm(user=request.user)

    return render(request, 'ferreteria/form_producto.html', {'form': form})


@login_required
def form_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('form_categoria')
    else:
        form = CategoriaForm()

    categorias = Categoria.objects.all()
    return render(
        request,
        'ferreteria/form_categoria.html',
        {
            'form': form,
            'categorias': categorias
        }
    )


@login_required
def form_proveedor(request):
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('form_proveedor')
    else:
        form = ProveedorForm()

    proveedores = Proveedor.objects.all()
    return render(
        request,
        'ferreteria/form_proveedor.html',
        {
            'form': form,
            'proveedores': proveedores
        }
    )


def ver_productos(request):
    productos = Producto.objects.all()
    return render(request, 'ferreteria/ver_productos.html', {'productos': productos})


def buscar_producto(request):
    productos = []
    query = request.GET.get('q')
    if query:
        productos = Producto.objects.filter(nombre__icontains=query)

    return render(request, 'ferreteria/buscar_producto.html', {'productos': productos})


def ver_proveedores(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'ferreteria/ver_proveedores.html', {'proveedores': proveedores})


def ver_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'ferreteria/ver_categorias.html', {'categorias': categorias})


def acerca(request):
    return render(request, 'ferreteria/acerca.html')

def detalle_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    context = {
        'producto': producto
    }
    return render(request, 'ferreteria/detalle_producto.html', context)

def editar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)

    if request.method == "POST":
        form = ProductoForm(
            request.POST,
            instance=producto,
            user=request.user
        )
        if form.is_valid():
            form.save()
            return redirect("ver_productos")
    else:
        form = ProductoForm(
            instance=producto,
            user=request.user
        )

    return render(
        request,
        "ferreteria/editar_producto.html",
        {
            "form": form,
            "producto": producto
        }
    )