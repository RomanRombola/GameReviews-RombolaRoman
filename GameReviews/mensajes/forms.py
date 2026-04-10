from django import forms
from .models import Message


class MensajeForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ["destinatario", "texto"]
        labels = {
            "destinatario": "Para",
            "texto": "Mensaje",
        }
        widgets = {
            "texto": forms.Textarea(attrs={"rows": 4}),
        }
