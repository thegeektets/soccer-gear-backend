import json

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from transaction.models import Order, Order_Item, Payment
from transaction.serializers import PaymentSerializer, OrderSerializer, Order_ItemSerializer

class OrderViewSet(viewsets.ModelViewSet):

    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (IsAuthenticated,)

class Order_ItemViewSet(viewsets.ModelViewSet):

    queryset = Order_Item.objects.all()
    serializer_class = Order_ItemSerializer
    permission_classes = (IsAuthenticated,)

class PaymentViewSet(viewsets.ModelViewSet):

    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = (IsAuthenticated,)