import json
import django_filters

from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated, AllowAny

from products.models import Product, Category
from products.serializers import ProductSerializer, CategorySerializer


class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = Product
        fields = ['title', 'price', ]


class ProductViewSet(viewsets.ModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (AllowAny,)
    filter_backends = (filters.SearchFilter, filters.DjangoFilterBackend)
    filter_class = ProductFilter
    search_fields = ('title', 'price', )


class CategoryViewSet(viewsets.ModelViewSet):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (AllowAny,)
