from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from users.models import Profile


class ProfileCreateForm(UserCreationForm):
    class Meta:
        model = Profile
        fields = ("username", "email")



class ProfileChangeForm(UserChangeForm):
    class Meta:
        model = Profile
        fields = ("avatar", "pais", "direccion", "fecha_de_nacimiento", "first_name", "last_name", "password")
        
        widgets = {
            "avatar": forms.ClearableFileInput(attrs={"class": "form-control"}),
            "pais": forms.TextInput(attrs={"class": "form-control"}),
            "direccion": forms.TextInput(attrs={"class": "form-control"}),
            "fecha_de_nacimiento": forms.DateInput(attrs={"class": "form-control"}),
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "password": forms.PasswordInput(attrs={"class": "form-control"})
        }

class ProfileChangeForm(forms.ModelForm):
    fecha_nacimiento = forms.DateField(
        required=False,
        widget=forms.DateInput(
            attrs={
                "type": "date",
                "class": "form-control form-control-sm"
            }
        )
    )

    class Meta:
        model = Profile
        fields = (
            "pais",
            "direccion",
            "fecha_nacimiento",
            "avatar",
        )
        widgets = {
            "pais": forms.TextInput(attrs={"class": "form-control form-control-sm"}),
            "direccion": forms.TextInput(attrs={"class": "form-control form-control-sm"}),
            "avatar": forms.FileInput(attrs={"class": "form-control form-control-sm"}),
        }
