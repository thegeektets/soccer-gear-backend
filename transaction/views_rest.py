import json

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from transaction.models import Order, Order_Item, Payment
from transaction.serializers import PaymentSerializer, OrderSerializer, OrderItemSerializer


class OrderViewSet(viewsets.ModelViewSet):

    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (IsAuthenticated,)


class OrderItemViewSet(viewsets.ModelViewSet):

    queryset = Order_Item.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = (IsAuthenticated,)


class PaymentViewSet(viewsets.ModelViewSet):

    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = (IsAuthenticated,)