# Generated by Django 5.0.6 on 2024-08-15 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_carrinho"),
    ]

    operations = [
        migrations.CreateModel(
            name="Caminho",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("nome", models.CharField(max_length=100)),
            ],
        ),
    ]