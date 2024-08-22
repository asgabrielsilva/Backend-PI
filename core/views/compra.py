from rest_framework.viewsets import ModelViewSet

from core.models import Compra
from core.serializers import CompraDetailSerializer, CompraSerializer


class CompraViewSet(ModelViewSet):
    queryset = Compra.objects.all()
    serializer_class = CompraSerializer

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return CompraDetailSerializer
        return CompraSerializer