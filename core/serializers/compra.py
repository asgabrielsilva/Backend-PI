from rest_framework.serializers import (
    CharField,
    CurrentUserDefault,
    DateTimeField,
    HiddenField,
    ModelSerializer,
    SerializerMethodField,
    ValidationError,
)

from core.models import Compra, ItensCompra

class ItensCompraSerializer(ModelSerializer):
    total = SerializerMethodField()

    def get_total(self, instance):
        return instance.produto.preco * instance.quantidade

    class Meta:
        model = ItensCompra
        fields = "__all__"
        depth = 1

class CriarEditarItensCompraSerializer(ModelSerializer):
    class Meta:
        model = ItensCompra
        fields = ("produto", "quantidade")

    def validate_quantidade(self, quantidade):
        if quantidade <= 0:
            raise ValidationError("Quantidade deve ser maior que zero.")
        return quantidade



class CompraSerializer(ModelSerializer):
    usuario = CharField(source="user.email", read_only=True)
    status = CharField(source="get_status_display", read_only=True)
    data = DateTimeField(read_only=True)
    tipo_pagamento = CharField(source="get_tipo_pagamento_display", read_only=True)
    itens = ItensCompraSerializer(read_only=True, many=True)

    class Meta:
        model = Compra
        fields = ("id", "usuario", "status", "total", "data", "tipo_pagamento", "itens")

class CriarEditarCompraSerializer(ModelSerializer):
    usuario = HiddenField(default=CurrentUserDefault())
    itens = CriarEditarItensCompraSerializer(many=True)
    
    class Meta:
        model = Compra
        fields = ("id", "usuario", "itens")
        
    def create(self, validated_data):
        itens = validated_data.pop("itens")
        usuario = validated_data["usuario"]

        compra, criada = Compra.objects.get_or_create(
            usuario=usuario, status=Compra.StatusCompra.CARRINHO, defaults=validated_data
        )

        for item in itens:
            item_existente = compra.itens.filter(produto=item["produto"]).first()

            if item_existente:
                item_existente.quantidade += item["quantidade"]
                item_existente.preco = item["produto"].preco
                item_existente.save()
            else:
                item["preco"] = item["produto"].preco
                ItensCompra.objects.create(compra=compra, **item)

        compra.save()
        return compra

    def update(self, compra, validated_data):
        itens = validated_data.pop("itens", [])
        if itens:
            compra.itens.all().delete()
            for item in itens:
                item["preco"] = item["produto"].preco
                ItensCompra.objects.create(compra=compra, **item)

        return super().update(compra, validated_data)

class ListarItensCompraSerializer(ModelSerializer):
    produto = CharField(source="produto.nome", read_only=True)

    class Meta:
        model = ItensCompra
        fields = "__all__"
        depth = 1

class ListarCompraSerializer(ModelSerializer):
    usuario = CharField(source="user.email", read_only=True)
    itens = ListarItensCompraSerializer(many=True, read_only=True)

    class Meta:
        model = Compra
        fields = "__all__"