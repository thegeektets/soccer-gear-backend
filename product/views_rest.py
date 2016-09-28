import json
import django_filters

from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated

from product.models import Product, Product_Category, Category
from product.serializers import ProductSerializer, CategorySerializer, ProductCategorySerializer


class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = Product
        fields = ['title', 'price', ]


class ProductViewSet(viewsets.ModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter, filters.DjangoFilterBackend)
    filter_class = ProductFilter
    search_fields = ('title', 'price', )


class Product_CategoryViewSet(viewsets.ModelViewSet):

    queryset = Product_Category.objects.all()
    serializer_class = ProductCategorySerializer
    permission_classes = (IsAuthenticated,)


class CategoryViewSet(viewsets.ModelViewSet):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAuthenticated,)
