from django.db import migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="contenido",
            field=ckeditor.fields.RichTextField(),
        ),
    ]
