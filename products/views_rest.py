import json
import django_filters

from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.db.models import Q

from products.models import Product, Category
from products.serializers import ProductSerializer, CategorySerializer
from soccer_gear.rest_extensions import CheckIfSuperUser
from rest_framework.exceptions import PermissionDenied


class ProductFilter(django_filters.FilterSet):

    category = django_filters.MethodFilter()

    def filter_category(self, queryset, value):
        q = Q(Q(category__id=value)|Q(category__parent_id=value))
        return queryset.filter(q)

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

    def list(self, request, *args, **kwargs):
        self.queryset = self.queryset.filter(parent=None)
        return super(CategoryViewSet, self).list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super(CategoryViewSet, self).retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        if request.user.is_superuser or request.user.is_admin:
            return super(CategoryViewSet, self).update(request, *args, **kwargs)
        else:
            raise PermissionDenied

    def destroy(self, request, *args, **kwargs):
        if request.user.is_superuser or request.user.is_admin:
            return super(CategoryViewSet, self).destroy(request, *args, **kwargs)
        else:
            raise PermissionDenied

    def create(self, request, *args, **kwargs):
        if request.user.is_superuser or request.user.is_admin:
            return super(CategoryViewSet, self).create(request, *args, **kwargs)
        else:
            raise PermissionDenied