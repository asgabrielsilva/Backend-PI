# Generated by Django 5.1 on 2024-12-10 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0017_compra_tipo_pagamento"),
    ]

    operations = [
        migrations.AddField(
            model_name="compra",
            name="total",
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
