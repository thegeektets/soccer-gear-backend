import json

from rest_framework import viewsets
from rest_framework.decorators import list_route
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from soccer_gear.settings import LIPISHA_API_KEY, LIPISHA_API_SIGNATURE

from transaction.models import Order, Order_Item, Payment
from transaction.serializers import PaymentSerializer, OrderSerializer, OrderItemSerializer
from lipisha import Lipisha


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


class CheckoutViewSet(viewsets.ViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = (IsAuthenticated,)

    @list_route(methods=['post',])
    def request_payment(self, request, *args, **kwargs):
        account_number = request.POST.get('account_number', None)
        mobile_number = request.POST.get('mobile_number', None)

        lipisha = Lipisha(LIPISHA_API_KEY, LIPISHA_API_SIGNATURE, api_environment='test')
        abc = lipisha.request_money(
                account_number="098000",
                mobile_number="1234567890",
                method="Paybill (M-Pesa)",
                amount="10",
                currency="KES",
                reference="O1212"
        )
        print(abc)
        return Response(abc)

    @list_route(methods=['post',])
    def confirm_transaction(self, request, *args, **kwargs):
        transaction = request.POST.get('transaction', None)

        lipisha = Lipisha(LIPISHA_API_KEY, LIPISHA_API_SIGNATURE, api_environment='test')
        abc = lipisha.confirm_transaction(
                transaction="WOACXI9D8"
        )
        print(abc)
        return Response(abc)
