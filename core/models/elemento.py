from django.db import models

class Elemento(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nome} - ({self.id})"