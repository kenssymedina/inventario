from django.urls import path
from .views import *

urlpatterns = [
    path('lista/', ArticuloListCreateAPIView.as_view(), name='articulo-listar')
]
