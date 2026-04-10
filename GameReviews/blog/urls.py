from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("about/", views.about, name="about"),
    path("pages/", views.PostListView.as_view(), name="posts"),
    path("pages/<int:pk>/", views.PostDetailView.as_view(), name="post_detalle"),
    path("pages/crear/", views.post_crear, name="post_crear"),
    path("pages/<int:pk>/editar/", views.PostUpdateView.as_view(), name="post_editar"),
    path("pages/<int:pk>/borrar/", views.PostDeleteView.as_view(), name="post_borrar"),
    path("buscar/", views.buscar, name="buscar"),
]
