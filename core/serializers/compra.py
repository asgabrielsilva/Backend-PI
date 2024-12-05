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
        # fields = ("produto", "quantidade")
        fields = "__all__"

    def validate_quantidade(self, quantidade):
        if quantidade <= 0:
            raise ValidationError("Quantidade deve ser maior que zero.")
        return quantidade

    def validate(self, item):
        if item["quantidade"] > item["produto"].quantidade:
            raise ValidationError({"Quantidade de itens maior do que a quantidade em estoque."})
        return item


class CompraSerializer(ModelSerializer):
    usuario = CharField(source="user.email", read_only=True)
    status = CharField(source="get_status_display", read_only=True)
    data = DateTimeField(read_only=True)
    itens = ItensCompraSerializer(read_only=True, many=True)

    class Meta:
        model = Compra
        # fields = ("id", "usuario", "status", "total", "data", "itens")
        fields = "__all__"

class CriarEditarCompraSerializer(ModelSerializer):
    usuario = HiddenField(default=CurrentUserDefault())
    itens = CriarEditarItensCompraSerializer(many=True)
    
    class Meta:
        model = Compra
        fields = "__all__"
        
    def create(self, validated_data):
        itens_data = validated_data.pop("itens")
        compra = Compra.objects.create(**validated_data)
        for item_data in itens_data:
            item_data["preco"] = item_data["produto"].preco
            ItensCompra.objects.create(compra=compra, **item_data)
        compra.save()
        return compra
    
    def update(self, compra, validated_data):
        itens_data = validated_data.pop("itens")
        if itens_data:
            compra.itens.all().delete()
            for item_data in itens_data:
                item_data["preco"] = item_data["produto"].preco
                ItensCompra.objects.create(compra=compra, **item_data)
        compra.save()
        return super().update(compra, validated_data)

class ListarItensCompraSerializer(ModelSerializer):
    produto = CharField(source="produto.nome", read_only=True)

    class Meta:
        model = ItensCompra
        # fields = ("id", "usuario", "status", "total", "itens")
        fields = "__all__"
        depth = 1

class ListarCompraSerializer(ModelSerializer):
    usuario = CharField(source="user.email", read_only=True)
    itens = ListarItensCompraSerializer(many=True, read_only=True)

    class Meta:
        model = Compra
        # fields = ("id", "usuario", "status", "total", "itens")
        fields = "__all__"
