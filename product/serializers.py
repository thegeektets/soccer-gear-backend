from rest_framework import serializers
from .models import Product, Category, ProductCategory


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'title')


class ProductCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductCategory
        fields = ('id', 'product_id', 'product', 'category_id', 'category')

    product_id = serializers.IntegerField()
    product = ProductSerializer(many=False, read_only=True)
    category_id = serializers.IntegerField()
    category = CategorySerializer(many=False, read_only=True)
