from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Email")
    first_name = forms.CharField(max_length=50, required=True, label="Nombre")
    last_name = forms.CharField(max_length=50, required=True, label="Apellido")

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password1", "password2"]


class EditarPerfilForm(forms.ModelForm):
    first_name = forms.CharField(max_length=50, required=False, label="Nombre")
    last_name = forms.CharField(max_length=50, required=False, label="Apellido")
    email = forms.EmailField(required=False, label="Email")

    class Meta:
        model = Profile
        fields = ["avatar", "bio", "fecha_nacimiento"]
        labels = {
            "avatar": "Foto de perfil",
            "bio": "Biografía",
            "fecha_nacimiento": "Fecha de nacimiento",
        }
        widgets = {
            "fecha_nacimiento": forms.DateInput(attrs={"type": "date"}),
            "bio": forms.Textarea(attrs={"rows": 4}),
        }
