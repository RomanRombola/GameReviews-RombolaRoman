from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="Post",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("titulo", models.CharField(max_length=200)),
                ("subtitulo", models.CharField(max_length=200)),
                ("contenido", models.TextField()),
                ("imagen", models.ImageField(blank=True, null=True, upload_to="posts/")),
                ("puntaje", models.IntegerField(choices=[(1, "1"), (2, "2"), (3, "3"), (4, "4"), (5, "5"), (6, "6"), (7, "7"), (8, "8"), (9, "9"), (10, "10")], default=5)),
                ("genero", models.CharField(blank=True, max_length=100)),
                ("fecha", models.DateField(auto_now_add=True)),
                ("autor", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="auth.user")),
            ],
            options={"ordering": ["-fecha"]},
        ),
    ]
