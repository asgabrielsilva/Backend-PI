from django.db import models

from .user import User
from .produto import Produto

class Compra(models.Model):
    class TipoPagamento(models.IntegerChoices):
        PIX = 1, "PIX"
        CARTAO_CREDITO = 2, "Cartão de Crédito"
        CARTAO_DEBITO = 3, "Cartão de Débito"
        BOLETO = 4, "Boleto"

    class StatusCompra(models.IntegerChoices):
        CARRINHO = 1, "Carrinho"
        REALIZADO = 2, "Realizado"
        PAGO = 3, "Pago"
        ENTREGUE = 4, "Entregue"

    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name="compras", blank=True, null=True)
    tipo_pagamento = models.IntegerField(choices=TipoPagamento.choices, default=TipoPagamento.PIX)
    status = models.IntegerField(choices=StatusCompra.choices,  default=StatusCompra.CARRINHO)
    data = models.DateTimeField(auto_now_add=True)

    @property
    def total(self):
        # total = 0
        # for item in self.itens.all():
        #     total += item.livro.preco * item.quantidade
        # return total
        return sum(item.preco * item.quantidade for item in self.itens.all())
    
class ItensCompra(models.Model):
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE, related_name="itens")
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT, related_name="+")
    quantidade = models.IntegerField(default=1)
    preco = models.DecimalField(max_digits=10, decimal_places=2, default=0)