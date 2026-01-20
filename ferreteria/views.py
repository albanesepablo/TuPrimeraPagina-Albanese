from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Producto, Proveedor, Categoria
from .forms import ProductoForm, CategoriaForm, ProveedorForm


def index(request):
    return render(request, 'ferreteria/index.html')


def inicio(request):
    return render(request, 'ferreteria/inicio.html')


@login_required
def form_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('ver_productos')
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

@login_required
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


@login_required
def eliminar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    producto.delete()
    return redirect("ver_productos")


@login_required
def eliminar_categoria(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    categoria.delete()
    return redirect("form_categoria")


@login_required
def editar_proveedor(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)

    if request.method == "POST":
        form = ProveedorForm(request.POST, instance=proveedor)
        if form.is_valid():
            form.save()
            return redirect('form_proveedor')
    else:
        form = ProveedorForm(instance=proveedor)

    return render(request, 'ferreteria/editar_proveedor.html', {
        'form': form
    })


@login_required
def eliminar_proveedor(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    proveedor.delete()
    return redirect("form_proveedor")