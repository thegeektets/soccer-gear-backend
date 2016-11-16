from django.contrib import admin
from products.models import Product, Category, FileUpload

admin.site.register(Product)
admin.site.register(FileUpload)
admin.site.register(Category)
