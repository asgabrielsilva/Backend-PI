from django.db import models

from .user import User

class Carrinho(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name="carrinhos", blank=True, null=True)
    total = models.DecimalField(max_digits=7, decimal_places=2, default=0, null=True, blank=True)

    def __str__(self):
        return f'{self.user} - {self.total} - ({self.id})'