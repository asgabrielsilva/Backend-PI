from rest_framework.serializers import ModelSerializer

from core.models import Raridade


class RaridadeSerializer(ModelSerializer):
    class Meta:
        model = Raridade
        fields = ('id', 'tier')