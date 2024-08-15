# Generated by Django 5.0.6 on 2024-08-15 11:40

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Carrinho",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("total", models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=7, null=True)),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="carrinhos",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]