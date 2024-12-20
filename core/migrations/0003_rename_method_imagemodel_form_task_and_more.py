# Generated by Django 5.1.3 on 2024-11-05 23:54

import core.models
import versatileimagefield.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0002_rename_imagefield_imagemodel"),
    ]

    operations = [
        migrations.RenameField(
            model_name="imagemodel",
            old_name="method",
            new_name="form_task",
        ),
        migrations.RemoveField(
            model_name="imagemodel",
            name="id",
        ),
        migrations.AddField(
            model_name="imagemodel",
            name="encrypt",
            field=models.IntegerField(default=1, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name="imagemodel",
            name="img_id",
            field=models.CharField(default=2, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="imagemodel",
            name="image",
            field=versatileimagefield.fields.VersatileImageField(
                upload_to=core.models.upload_to_folder
            ),
        ),
    ]
