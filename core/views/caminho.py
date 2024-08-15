from rest_framework.viewsets import ModelViewSet

from core.models import Caminho
from core.serializers import CaminhoSerializer


class CaminhoViewSet(ModelViewSet):
    queryset = Caminho.objects.all()
    serializer_class = CaminhoSerializer