from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="Message",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("texto", models.TextField()),
                ("fecha", models.DateTimeField(auto_now_add=True)),
                ("destinatario", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="mensajes_recibidos", to="auth.user")),
                ("remitente", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="mensajes_enviados", to="auth.user")),
            ],
            options={"ordering": ["-fecha"]},
        ),
    ]
