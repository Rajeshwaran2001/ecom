from rest_framework import viewsets
from rest_framework import generics
from .serializers import ProductSerializer
from .models import Product
from rest_framework import filters
# Create your views here.


class ProductViewSet(viewsets.ModelViewSet):
    search_fields = ['name']
    filter_backends = (filters.SearchFilter,)
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductSerializer