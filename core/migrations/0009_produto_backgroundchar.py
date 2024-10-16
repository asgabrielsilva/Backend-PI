# Generated by Django 5.1 on 2024-08-30 19:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0008_alter_produto_caminho_alter_produto_elemento_and_more"),
        ("uploader", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="produto",
            name="backgroundChar",
            field=models.ForeignKey(
                blank=True,
                default=None,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="uploader.image",
            ),
        ),
    ]
