# GameReviews — Rombola Román

Blog de reseñas de videojuegos desarrollado con Django como entrega final del curso de Python en CoderHouse.

## Tecnologías

- Python 3.x
- Django 5.x
- SQLite
- Pillow (imágenes)

## Instalación

```bash
# 1. Clonar el repositorio
git clone https://github.com/TU_USUARIO/TuPrimeraPagina-RombolaRoman.git
cd TuPrimeraPagina-RombolaRoman/GameReviews

# 2. Crear entorno virtual
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Linux / Mac

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Aplicar migraciones
python manage.py migrate

# 5. Crear superusuario (opcional, para el admin)
python manage.py createsuperuser

# 6. Iniciar el servidor
python manage.py runserver
```

Abrir en: http://127.0.0.1:8000/

## Orden de prueba

### 1. Registro e ingreso
- Ir a `/accounts/registro/` y crear una cuenta
- O usar `/accounts/login/` si ya tenés una

### 2. Crear una reseña
- Una vez logueado, hacer clic en **+ Nueva Reseña** en el navbar
- Completar título, subtítulo, contenido, puntaje, género e imagen (opcional)
- Guardar

### 3. Ver reseñas
- `/posts/` muestra todas las reseñas con paginación
- Hacer clic en **Leer más** para ver el detalle completo

### 4. Editar y borrar
- Solo el autor de cada reseña ve los botones de editar y borrar en el detalle

### 5. Buscar reseñas
- Ir a **Buscar** en el navbar o a `/buscar/`
- Buscar por parte del título

### 6. Perfil
- Hacer clic en tu nombre de usuario en el navbar
- Editar nombre, apellido, email, bio, foto de perfil y fecha de nacimiento

### 7. Admin
- Acceder en `/admin/` con el superusuario creado

## Estructura

```
GameReviews/
├── GameReviews/        ← configuración del proyecto
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── blog/               ← app de reseñas
│   ├── models.py       ← Post
│   ├── views.py        ← FBV + CBV (ListView, DetailView, UpdateView, DeleteView)
│   ├── forms.py
│   └── urls.py
├── accounts/           ← app de usuarios
│   ├── models.py       ← Profile (OneToOne con User)
│   ├── views.py
│   ├── forms.py
│   └── urls.py
├── templates/          ← herencia desde base.html
├── static/css/
├── media/              ← imágenes subidas
└── manage.py
```

## Funcionalidades

- CRUD completo de reseñas (crear, listar, ver detalle, editar, borrar)
- Autenticación: registro, login, logout
- Perfil de usuario con avatar y bio
- Búsqueda de reseñas por título
- Paginación en el listado
- Restricción de acceso: editar/borrar solo si sos el autor
- Herencia de templates desde `base.html`
- CBV: `ListView`, `DetailView`, `UpdateView`, `DeleteView`
- Decorador `@login_required` y mixin `LoginRequiredMixin`
