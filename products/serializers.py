from rest_framework import serializers
from .models import Product, Category

class ChildCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'title', 'parent')

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'title', 'parent', 'categories')

    categories = ChildCategorySerializer(source="get_children", many=True)

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product

    main_image = serializers.CharField(allow_blank=True)
    



