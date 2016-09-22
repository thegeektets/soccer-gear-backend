from django.contrib import admin
from transaction.models import Order, Order_Item, Payment

admin.site.register(Order)
admin.site.register(Order_Item)
admin.site.register(Payment)
