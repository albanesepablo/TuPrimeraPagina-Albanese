from django.shortcuts import render, redirect
from .models import Producto, Categoria, Proveedor
from .forms import ProductoForm, CategoriaForm, ProveedorForm

def inicio(request):
    return render(request, 'ferreteria/inicio.html')

# Formulario Producto
def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = ProductoForm()
    return render(request, 'ferreteria/form_producto.html', {'form': form})

# Formulario Categoría
def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = CategoriaForm()
    return render(request, 'ferreteria/form_categoria.html', {'form': form})

# Formulario Proveedor
def crear_proveedor(request):
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = ProveedorForm()
    return render(request, 'ferreteria/form_proveedor.html', {'form': form})

# Buscar Producto
def buscar_producto(request):
    productos = None
    if 'nombre' in request.GET:
        nombre = request.GET['nombre']
        productos = Producto.objects.filter(nombre__icontains=nombre)
    return render(request, 'ferreteria/buscar_producto.html', {'productos': productos})
