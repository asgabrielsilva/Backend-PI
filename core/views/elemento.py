from rest_framework.viewsets import ModelViewSet

from core.models import Elemento
from core.serializers import ElementoSerializer


class ElementoViewSet(ModelViewSet):
    queryset = Elemento.objects.all()
    serializer_class = ElementoSerializer