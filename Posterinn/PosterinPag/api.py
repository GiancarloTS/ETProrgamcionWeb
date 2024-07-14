from .models import Producto
from rest_framework import viewsets, permissions
from .serializers import ProductoSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all() #Conjunto de datos
    permission_classes = [permissions.AllowAny]
    serializer_class = ProductoSerializer