from django.db import models

from .caminho import Caminho
from .elemento import Elemento
from .raridade import Raridade

class Produto(models.Model):
    class RaridadeProduto(models.IntegerChoices):
        QUATRO = 4, "4 Estrelas"
        CINCO = 5, "5 Estrelas"

    nome = models.CharField(max_length=255)
    descricao = models.CharField(max_length=32, null=True, blank=True)
    preco = models.DecimalField(max_digits=7, decimal_places=2, default=0, null=True, blank=True, verbose_name="Preço")
    caminho = models.ForeignKey(Caminho, on_delete=models.PROTECT, related_name="produtos", blank=True, null=True)
    elemento = models.ForeignKey(Elemento, on_delete=models.PROTECT, related_name="produtos", blank=True, null=True)
    tier = models.IntegerField(choices=RaridadeProduto.choices,  default=RaridadeProduto.QUATRO)

    def __str__(self):
        return f"({self.id}) {self.nome} ({self.descricao})"