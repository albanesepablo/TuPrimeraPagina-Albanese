from django import forms
from .models import Novedad

class NovedadForm(forms.ModelForm):
    class Meta:
        model = Novedad
        fields = [
            "titulo",
            "subtitulo",
            "imagen",
            "codigo",
            "contenido",
        ]
        widgets = {
            "titulo": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Título de la novedad"
            }),
            "subtitulo": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Subtítulo"
            }),
            "codigo": forms.NumberInput(attrs={
                "class": "form-control",
                "placeholder": "Código único"
            }),
            "contenido": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 4,
                "placeholder": "Contenido de la novedad"
            }),
        }
