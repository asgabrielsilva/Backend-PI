from rest_framework.serializers import ModelSerializer, SlugRelatedField

from uploader.models import Image
from uploader.serializers import ImageSerializer

from core.models import Produto

class ProdutoDetailSerializer(ModelSerializer): 
    backgroundChar = ImageSerializer(required=False)
    caminhoPng = ImageSerializer(required=False)
    elementoPng = ImageSerializer(required=False)

    class Meta:
        model = Produto
        fields = "__all__"
        depth = 1

class ProdutoListSerializer(ModelSerializer):
    backgroundChar = ImageSerializer(
        required=False,
        read_only=True
    )
    class Meta:
        model = Produto
        fields = ("id", "nome", "preco", "backgroundChar")

class ProdutoSerializer(ModelSerializer):
    backgroundChar_attachment_key = SlugRelatedField(
        source="backgroundChar",
        queryset=Image.objects.all(),
        slug_field="attachment_key",
        required=False,
        write_only=True,
    )
    backgroundChar = ImageSerializer(
        required=False,
        read_only=True
    )
    caminhoPng_attachment_key = SlugRelatedField(
        source="caminhoPng",
        queryset=Image.objects.all(),
        slug_field="attachment_key",
        required=False,
        write_only=True,
    )
    caminhoPng = ImageSerializer(
        required=False,
        read_only=True
    )
    elementoPng_attachment_key = SlugRelatedField(
        source="elementoPng",
        queryset=Image.objects.all(),
        slug_field="attachment_key",
        required=False,
        write_only=True,
    )
    elementoPng = ImageSerializer(
        required=False,
        read_only=True
    )
    class Meta:
        model = Produto
        fields = "__all__"