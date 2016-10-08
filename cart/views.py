import json

from cart.models import Cart, CartItem
from cart.serializers import CartSerializer

# Create your views here.
from django.contrib.auth.models import AnonymousUser
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import viewsets
from rest_framework.decorators import list_route, detail_route
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from soccer_gear.rest_extensions import SetToUserOrSuper


class CartViewSet(viewsets.ModelViewSet, SetToUserOrSuper):

    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = (AllowAny,)

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_anonymous():
            if not request.session.get('has_session'):
                request.session.create()
                request.session['has_session'] = True
                request.session.save()
        return super(CartViewSet, self).dispatch(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        self.queryset = self.set_to_user_or_super(request, self.queryset)
        return super(CartViewSet, self).create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        self.queryset = self.set_to_user_or_super(request, self.queryset)
        return super(CartViewSet, self).update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        self.queryset = self.set_to_user_or_super(request, self.queryset)
        return super(CartViewSet, self).destroy(request, *args, **kwargs)

    @list_route(methods=['GET',])
    def my_cart(self, request, *args, **kwargs):
        cart = Cart.objects.get_for_user_or_session(request.user, request.session.session_key)
        if cart is not None:
            return Response(self.serializer_class(cart).data)
        else:
            return Response(self.serializer_class(cart).data)

    @detail_route(methods=['POST',])
    def add_item(self, request, *args, **kwargs):
        cart = Cart.objects.get_or_create_for_user_or_session(request.user, request.session.session_key)
        print(request.data)
        product_id = request.data.get('product_id', None)
        chosen_attributes = request.data.get('chosen_attributes', {})
        if product_id:
            cart = cart.add_item(product_id, chosen_attributes)

        return Response(self.serializer_class(cart).data)

    @detail_route(methods=['POST',])
    def remove_item(self, request, *args, **kwargs):
        cart = Cart.objects.get_or_create_for_user_or_session(request.user, request.session.session_key)
        cart_item_id = request.data.get('cart_item_id', None)
        if cart_item_id:
            cart = cart.remove_item(cart_item_id)

        return Response(self.serializer_class(cart).data)

    @detail_route(methods=['POST',])
    def set_quantity(self, request, *args, **kwargs):
        cart = Cart.objects.get_or_create_for_user_or_session(request.user, request.session.session_key)
        cart_item_id = request.data.get('cart_item_id', None)
        quantity = request.data.get('quantity', None)
        quantity = int(quantity)
        if cart_item_id:
            cart.update_quantity_for_item(cart_item_id, quantity)

        return Response(self.serializer_class(cart).data)
