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
        fields = ('id', 'status', 'payment', 'cost', 'user_id')

    user_id = serializers.IntegerField()
    payment = PaymentSerializer(many=False, read_only=True)


class OrderItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order_Item
        fields = ('id', 'order_id', 'order', 'product_id', 'products', 'price', 'quantity', 'user_id' )

    user_id = serializers.IntegerField()
    order_id = serializers.IntegerField()
    order = OrderSerializer(many=False, read_only=True)
    product_id = serializers.IntegerField()
    product = ProductSerializer(many=False, read_only=True)