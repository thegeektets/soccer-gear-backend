import json

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from product.models import Product, Product_Category, Category
from product.serializers import ProductSerializer, CategorySerializer, Product_CategorySerializer

class ProductViewSet(viewsets.ModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated,)

class Product_CategoryViewSet(viewsets.ModelViewSet):

    queryset = Product_Category.objects.all()
    serializer_class = Product_CategorySerializer
    permission_classes = (IsAuthenticated,)

class CategoryViewSet(viewsets.ModelViewSet):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAuthenticated,)