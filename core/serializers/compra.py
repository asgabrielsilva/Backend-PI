from rest_framework.serializers import ModelSerializer

from core.models import Compra

class CompraSerializer(ModelSerializer):
    class Meta:
        model = Compra
        fields = "__all__"

class CompraDetailSerializer(ModelSerializer):
    class Meta:
        model = Compra
        fields = "__all__"
        depth = 1