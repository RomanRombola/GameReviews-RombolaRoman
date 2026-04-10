from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Message
from .forms import MensajeForm


@login_required
def bandeja_entrada(request):
    mensajes = Message.objects.filter(destinatario=request.user)
    return render(request, "mensajes/bandeja_entrada.html", {"mensajes": mensajes})


@login_required
def enviar_mensaje(request):
    if request.method == "POST":
        form = MensajeForm(request.POST)
        if form.is_valid():
            mensaje = form.save(commit=False)
            mensaje.remitente = request.user
            mensaje.save()
            return redirect("bandeja_entrada")
    else:
        form = MensajeForm()
    return render(request, "mensajes/enviar_mensaje.html", {"form": form})
