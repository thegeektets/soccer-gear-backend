from rest_framework import serializers
from .models import Product, Category, FileUpload

class FileUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileUpload

    datafile=serializers.CharField(read_only=True)


class ChildCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'title', 'parent')

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'title', 'parent', 'categories', 'parent_id')

    categories = ChildCategorySerializer(source="get_children", many=True, read_only=True)
    parent = ChildCategorySerializer(many=False, read_only=True, default=None)
    parent_id = serializers.IntegerField(read_only=True,)

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product

    datafile = FileUploadSerializer(many=False, read_only=True)
    datafile_id = serializers.IntegerField()
    category = CategorySerializer(many=False, read_only=True)
    category_id = serializers.IntegerField()






