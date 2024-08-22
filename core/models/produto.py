from django.db import models

from .caminho import Caminho
from .elemento import Elemento
from .raridade import Raridade

class Produto(models.Model):
    class RaridadeProduto(models.IntegerChoices):
        QUATRO = 4, "4 Estrelas"
        CINCO = 5, "5 Estrelas"

    class CaminhoProduto(models.IntegerChoices):
        HARMONIA = 1, "Cartão de Crédito"
        CARTAO_DEBITO = 2, "Cartão de Débito"
        PIX = 3, "PIX"
        BOLETO = 4, "Boleto"
        TRANSFERENCIA_BANCARIA = 5, "Transferência Bancária"
        DINHEIRO = 6, "Dinheiro"
        OUTRO = 7, "Outro"
    
    class ElementoProduto(models.IntegerChoices):
        CARTAO_CREDITO = 1, "Cartão de Crédito"
        CARTAO_DEBITO = 2, "Cartão de Débito"
        PIX = 3, "PIX"
        BOLETO = 4, "Boleto"
        TRANSFERENCIA_BANCARIA = 5, "Transferência Bancária"
        DINHEIRO = 6, "Dinheiro"
        OUTRO = 7, "Outro"

    nome = models.CharField(max_length=255)
    descricao = models.CharField(max_length=32, null=True, blank=True)
    preco = models.DecimalField(max_digits=7, decimal_places=2, default=0, null=True, blank=True, verbose_name="Preço")
    caminho = models.ForeignKey(Caminho, on_delete=models.PROTECT, related_name="produtos", blank=True, null=True)
    elemento = models.ForeignKey(Elemento, on_delete=models.PROTECT, related_name="produtos", blank=True, null=True)
    caminho = models.IntegerField(choices=CaminhoProduto.choices, default=CaminhoProduto.CARTAO_CREDITO)
    elemento = models.IntegerField(choices=ElementoProduto.choices, default=ElementoProduto.CARTAO_CREDITO)
    tier = models.IntegerField(choices=RaridadeProduto.choices,  default=RaridadeProduto.QUATRO)

    def __str__(self):
        return f"({self.id}) {self.nome} ({self.descricao})"