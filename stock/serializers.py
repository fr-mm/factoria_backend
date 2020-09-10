from rest_framework import serializers
from stock.models import Produto


class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        exclude = []
