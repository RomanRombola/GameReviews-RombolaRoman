from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from .models import Post
from .forms import PostForm, BusquedaForm


# --- Inicio ---

def inicio(request):
    posts_recientes = Post.objects.all()[:6]
    return render(request, "blog/inicio.html", {"posts": posts_recientes})


# --- About ---

def about(request):
    return render(request, "blog/about.html")


# --- Listado (CBV) ---

class PostListView(ListView):
    model = Post
    template_name = "blog/posts.html"
    context_object_name = "posts"
    paginate_by = 9


# --- Detalle (CBV) ---

class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detalle.html"
    context_object_name = "post"


# --- Crear (FBV con login_required) ---

@login_required
def post_crear(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.save()
            return redirect("post_detalle", pk=post.pk)
    else:
        form = PostForm()
    return render(request, "blog/post_form.html", {"form": form, "titulo": "Nueva Reseña"})


# --- Editar (LoginRequiredMixin + CBV) ---

from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post_form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo"] = "Editar Reseña"
        return context

    def get_success_url(self):
        return reverse_lazy("post_detalle", kwargs={"pk": self.object.pk})


# --- Borrar (LoginRequiredMixin + CBV) ---

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = "blog/post_confirmar_borrar.html"
    success_url = reverse_lazy("posts")


# --- Búsqueda ---

def buscar(request):
    form = BusquedaForm(request.GET or None)
    resultados = None
    if form.is_valid():
        titulo = form.cleaned_data.get("titulo", "")
        resultados = Post.objects.filter(titulo__icontains=titulo)
    return render(request, "blog/buscar.html", {"form": form, "resultados": resultados})
