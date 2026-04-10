from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):
    remitente = models.ForeignKey(User, on_delete=models.CASCADE, related_name="mensajes_enviados")
    destinatario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="mensajes_recibidos")
    texto = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"De {self.remitente} a {self.destinatario} ({self.fecha.strftime('%d/%m/%Y')})"

    class Meta:
        ordering = ["-fecha"]
