from rest_framework.viewsets import ModelViewSet

from core.models import Raridade
from core.serializers import RaridadeSerializer


class RaridadeViewSet(ModelViewSet):
    queryset = Raridade.objects.all()
    serializer_class = RaridadeSerializer