from rest_framework import serializers

from .models import Order, Order_Item, Payment
from products.models import  Product
from products.serializers import ProductSerializer


class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = ('id','mpesa_code','user_id')

    user_id = serializers.IntegerField()


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ('id', 'status', 'payment_id', 'cost', 'user_id')

    user_id = serializers.IntegerField()
    payment_id = serializers.IntegerField(required=False)


class OrderItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order_Item
        fields = ('id', 'order_id', 'product_id', 'price', 'quantity', 'user_id' )

    user_id = serializers.IntegerField()
    order_id = serializers.IntegerField()
    product_id = serializers.IntegerField()
    price = serializers.IntegerField()
    quantity = serializers.IntegerField()

