from django.contrib import admin
from product.models import Product, Category, Product_Category

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Product_Category)

