from django.db import models

from .user import User

class Compra(models.Model):
    class StatusCompra(models.IntegerChoices):
        CARRINHO = 1, "Carrinho"
        REALIZADO = 2, "Realizado"
        PAGO = 3, "Pago"
        ENTREGUE = 4, "Entregue"

    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name="compras", blank=True, null=True)
    total = models.DecimalField(max_digits=7, decimal_places=2, default=0, null=True, blank=True)
    status = models.IntegerField(choices=StatusCompra.choices,  default=StatusCompra.CARRINHO)

    def __str__(self):
        return f'{self.user} - {self.total} - {self.status} - ({self.id})'