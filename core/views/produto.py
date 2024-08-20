from rest_framework.viewsets import ModelViewSet

from core.models import Produto
from core.serializers import ProdutoDetailSerializer, ProdutoListSerializer, ProdutoSerializer


class ProdutoViewSet(ModelViewSet):
    queryset = Produto.objects.order_by("nome")
    serializer_class = ProdutoSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return ProdutoListSerializer
        elif self.action == "retrieve":
            return ProdutoDetailSerializer
        return ProdutoSerializer