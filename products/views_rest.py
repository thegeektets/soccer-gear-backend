import json
import django_filters

from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated, AllowAny

from products.models import Product, Category
from products.serializers import ProductSerializer, CategorySerializer
from soccer_gear.rest_extensions import CheckIfSuperUser


class ProductFilter(django_filters.FilterSet):

    color = django_filters.MethodFilter()

    def filter_color(self, queryset, value):
        return queryset.filter(color__contains=json.dumps([value]))

    size = django_filters.MethodFilter()

    def filter_size(self, queryset, value):
        return queryset.filter(size__contains=json.dumps([value]))

    class Meta:
        model = Product
        fields = ['title', 'price', 'category', ]


class ProductViewSet(viewsets.ModelViewSet, CheckIfSuperUser):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (AllowAny,)
    filter_backends = (filters.SearchFilter, filters.DjangoFilterBackend)
    filter_class = ProductFilter
    search_fields = ('title', 'price', 'description', 'category__title')

    def create(self, request, *args, **kwargs):
        self.check_if_superuser(request)
        return super(ProductViewSet, self).create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        self.check_if_superuser(request)
        return super(ProductViewSet, self).update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        self.check_if_superuser(request)
        return super(ProductViewSet, self).destroy(request, *args, **kwargs)

class CategoryViewSet(viewsets.ModelViewSet):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (AllowAny,)
