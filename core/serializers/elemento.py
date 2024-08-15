from rest_framework.serializers import ModelSerializer

from core.models import Elemento


class ElementoSerializer(ModelSerializer):
    class Meta:
        model = Elemento
        fields = ('id', 'nome')