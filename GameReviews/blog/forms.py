from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["titulo", "subtitulo", "contenido", "imagen", "puntaje", "genero"]
        labels = {
            "titulo": "Título del juego",
            "subtitulo": "Subtítulo o plataforma",
            "contenido": "Reseña",
            "imagen": "Imagen de portada",
            "puntaje": "Puntaje (1-10)",
            "genero": "Género",
        }
        widgets = {
            "titulo": forms.TextInput(attrs={"maxlength": 80}),
            "subtitulo": forms.TextInput(attrs={"maxlength": 80}),
            "genero": forms.TextInput(attrs={"maxlength": 50}),
            "contenido": forms.Textarea(attrs={"rows": 8}),
        }


class BusquedaForm(forms.Form):
    titulo = forms.CharField(
        max_length=200,
        label="Buscar por título",
        required=False,
    )
