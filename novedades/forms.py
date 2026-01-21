from django import forms
from .models import Novedad

class NovedadForm(forms.ModelForm):
    class Meta:
        model = Novedad
        fields = [
            "titulo",
            "subtitulo",
            "imagen",
            "nro_novedad",
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
            "nro_novedad": forms.NumberInput(attrs={
                "class": "form-control",
                "placeholder": "Número"
            }),
            "contenido": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 4,
                "placeholder": "Contenido de la novedad"
            }),
        }
