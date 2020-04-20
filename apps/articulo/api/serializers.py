from rest_framework import serializers
from ..models import Articulo

class ArticuloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articulo
        fields = ('codigoArticulo', 'nombre', 'tipo', 'fabricante', 'upc', 'marca', 'unidad', 'especificaciones')