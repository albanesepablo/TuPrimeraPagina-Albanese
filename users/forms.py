from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from users.models import Profile


class ProfileCreateForm(UserCreationForm):
    username = forms.CharField(
        label="Usuario",
        widget=forms.TextInput(attrs={"class": "form-control"})
    )

    email = forms.EmailField(
        label="Correo electrónico",
        widget=forms.EmailInput(attrs={"class": "form-control"})
    )

    password1 = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
        help_text="La contraseña debe tener al menos 8 caracteres."
    )

    password2 = forms.CharField(
        label="Confirmar contraseña",
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
        help_text="Ingresá la misma contraseña para verificar."
    )

    class Meta:
        model = Profile
        fields = ("username", "email")


class ProfileChangeForm(UserChangeForm):
    password = forms.CharField(
        label="Contraseña actual",
        widget=forms.PasswordInput(attrs={"class": "form-control form-control-sm"}),
        help_text="Ingresá tu contraseña actual para confirmar los cambios."
    )

    class Meta:
        model = Profile
        fields = (
            "avatar",
            "pais",
            "direccion",
            "fecha_de_nacimiento",
            "first_name",
            "last_name",
            "password",
        )

        labels = {
            "avatar": "Avatar",
            "pais": "País",
            "direccion": "Dirección",
            "fecha_de_nacimiento": "Fecha de nacimiento",
            "first_name": "Nombre",
            "last_name": "Apellido",
        }

        widgets = {
            "avatar": forms.ClearableFileInput(
                attrs={"class": "form-control form-control-sm"}
            ),
            "pais": forms.TextInput(
                attrs={"class": "form-control form-control-sm"}
            ),
            "direccion": forms.TextInput(
                attrs={"class": "form-control form-control-sm"}
            ),
            "fecha_de_nacimiento": forms.DateInput(
                attrs={
                    "type": "date",
                    "class": "form-control form-control-sm",
                }
            ),
            "first_name": forms.TextInput(
                attrs={"class": "form-control form-control-sm"}
            ),
            "last_name": forms.TextInput(
                attrs={"class": "form-control form-control-sm"}
            ),
        }
