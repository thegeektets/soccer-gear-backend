from cart.models import Cart, CartItem
from products.serializers import ProductSerializer
from rest_framework import serializers


class CartItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = CartItem

    product_id = serializers.IntegerField()
    product = ProductSerializer(read_only=True)

class CartSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cart

    items = CartItemSerializer(many=True)