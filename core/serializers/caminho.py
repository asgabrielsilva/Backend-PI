from rest_framework.serializers import ModelSerializer

from core.models import Caminho


class CaminhoSerializer(ModelSerializer):
    class Meta:
        model = Caminho
        fields = ('id', 'nome')