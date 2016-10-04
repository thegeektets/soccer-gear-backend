import json
import django_filters

from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated, AllowAny

from product.models import Product, ProductCategory, Category
from product.serializers import ProductSerializer, CategorySerializer, ProductCategorySerializer


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

    def create(self, request, *args, **kwargs):
        self.check_if_superuser(request)
        self.set_user_on_data(request)
        return super(ProductViewSet, self).create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        self.check_if_superuser(request)
        self.set_user_on_data(request)
        return super(ProductViewSet, self).update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        self.check_if_superuser(request)
        return super(ProductViewSet, self).destroy(request, *args, **kwargs)

class Product_CategoryViewSet(viewsets.ModelViewSet):

    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer
    permission_classes = (AllowAny,)


class CategoryViewSet(viewsets.ModelViewSet):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (AllowAny,)
