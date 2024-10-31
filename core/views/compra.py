from rest_framework.viewsets import ModelViewSet

from core.models import Compra
from core.serializers import CompraSerializer, CriarEditarCompraSerializer, ListarCompraSerializer


class CompraViewSet(ModelViewSet):
    # queryset = Compra.objects.order_by("-id")
    # serializer_class = CompraSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Compra.objects.order_by("-id")
        if user.groups.filter(name="administradores"):
            return Compra.objects.order_by("-id")
        return Compra.objects.filter(user=user).order_by("-id")

    
    def get_serializer_class(self):
        if self.action == "list":
            return ListarCompraSerializer
        if self.action in ("create", "update"):
            return CriarEditarCompraSerializer
        return CompraSerializer