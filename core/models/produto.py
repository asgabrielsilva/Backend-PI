from django.db import models

from uploader.models import Image

class Produto(models.Model):
    class RaridadeProduto(models.IntegerChoices):
        QUATRO = 4, "4 Estrelas"
        CINCO = 5, "5 Estrelas"

    class CaminhoProduto(models.IntegerChoices):
        DESTRUICAO = 1, "A Destruição"
        CACA = 2, "A Caça"
        ERUDICAO = 3, "A Erudição"
        HARMONIA = 4, "A Harmonia"
        INEXISTENCIA = 5, "A Inexistência"
        PRESERVACAO = 6, "A Preservação"
        ABUNDANCIA = 7, "A Abundância"
    
    class ElementoProduto(models.IntegerChoices):
        FISICO = 1, "Físico"
        FOGO = 2, "Fogo"
        GELO = 3, "Gelo"
        RAIO = 4, "Raio"
        VENTO = 5, "Vento"
        QUANTICO = 6, "Quântico"
        IMAGINARIO = 7, "Imaginário"

    nome = models.CharField(max_length=255)
    descricao = models.CharField(max_length=1000, null=True, blank=True)
    preco = models.DecimalField(max_digits=7, decimal_places=2, default=0, null=True, blank=True, verbose_name="Preço")
    caminho = models.IntegerField(choices=CaminhoProduto.choices, default=CaminhoProduto.DESTRUICAO)
    elemento = models.IntegerField(choices=ElementoProduto.choices, default=ElementoProduto.FISICO)
    tier = models.IntegerField(choices=RaridadeProduto.choices,  default=RaridadeProduto.QUATRO)
    backgroundChar = models.ForeignKey(
        Image,
        related_name="+",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        default=None,
    )
    caminhoPng = models.ForeignKey(
        Image,
        related_name="+",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        default=None,
    )
    elementoPng = models.ForeignKey(
        Image,
        related_name="+",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        default=None,
    )

    def __str__(self):
        return f"({self.id}) {self.nome} ({self.descricao})"