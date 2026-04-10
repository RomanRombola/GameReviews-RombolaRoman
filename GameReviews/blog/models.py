from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class Post(models.Model):
    PUNTAJE_CHOICES = [(i, str(i)) for i in range(1, 11)]

    titulo = models.CharField(max_length=80)
    subtitulo = models.CharField(max_length=80)
    contenido = RichTextField()
    imagen = models.ImageField(upload_to="posts/", blank=True, null=True)
    puntaje = models.IntegerField(choices=PUNTAJE_CHOICES, default=5)
    genero = models.CharField(max_length=100, blank=True)
    fecha = models.DateField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

    class Meta:
        ordering = ["-fecha"]
