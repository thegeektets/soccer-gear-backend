from rest_framework import serializers
from .models import Product, Category, Product_Category


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'title')


class Product_CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Product_Category
        fields = ('id','product_id','product','category_id', 'category')

    product_id = serializers.IntegerField()
    product = ProductSerializer(many=False, read_only=True)
    category_id = serializers.IntegerField()
    category = CategorySerializer(many=False, read_only=True)
