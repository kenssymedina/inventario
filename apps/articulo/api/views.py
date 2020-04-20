from rest_framework.generics import(
    ListAPIView,
    CreateAPIView,
    DestroyAPIView,
    UpdateAPIView,
    ListCreateAPIView,
    RetrieveAPIView
)

from .serializers import ArticuloSerializer
from ..models import Articulo


class ArticuloListCreateAPIView(ListCreateAPIView):
    queryset = Articulo.objects.all().order_by('codigoArticulo')
    serializer_class = ArticuloSerializer
