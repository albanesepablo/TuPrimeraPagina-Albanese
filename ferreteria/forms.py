from django import forms
from .models import Producto, Categoria, Proveedor


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = [
            "nombre",
            "precio",
            "categoria",
            "proveedor",
        ]
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "precio": forms.NumberInput(attrs={"class": "form-control"}),
            "categoria": forms.Select(attrs={"class": "form-select"}),
            "proveedor": forms.Select(attrs={"class": "form-select"}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)

        # Querysets explícitos (buena práctica)
        self.fields["categoria"].queryset = Categoria.objects.all()

        if not user or not user.is_authenticated:
            self.fields.pop("proveedor")
        else:
            self.fields["proveedor"].queryset = Proveedor.objects.all()


class ProductoUpdateForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = [
            "precio",
            "categoria",
            "proveedor",
        ]
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
            'proveedor': forms.TextInput(attrs={'class': 'form-control'}),
#            'fecha_de_creacion': forms.DateInput(attrs={'class': 'form-control'})
        }

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre']


class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['nombre', 'telefono', 'email']
