from rest_framework.serializers import ModelSerializer

from core.models import Carrinho

class CarrinhoSerializer(ModelSerializer):
    class Meta:
        model = Carrinho
        fields = "__all__"

class CarrinhoDetailSerializer(ModelSerializer):
    class Meta:
        model = Carrinho
        fields = "__all__"
        depth = 1