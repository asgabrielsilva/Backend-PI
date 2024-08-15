from rest_framework.viewsets import ModelViewSet

from core.models import Carrinho
from core.serializers import CarrinhoSerializer, CarrinhoDetailSerializer


class CarrinhoViewSet(ModelViewSet):
    queryset = Carrinho.objects.all()
    serializer_class = CarrinhoSerializer

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return CarrinhoDetailSerializer
        return CarrinhoSerializer