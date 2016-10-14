import json

from rest_framework import viewsets
from rest_framework.decorators import list_route
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from soccer_gear.settings import LIPISHA_API_KEY, LIPISHA_API_SIGNATURE

from transaction.models import Order, Order_Item, Payment
from transaction.serializers import PaymentSerializer, OrderSerializer, OrderItemSerializer
from lipisha import Lipisha


class OrderViewSet(viewsets.ModelViewSet):

    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (AllowAny,)


class OrderItemViewSet(viewsets.ModelViewSet):

    queryset = Order_Item.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = (AllowAny,)


class PaymentViewSet(viewsets.ModelViewSet):

    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = (AllowAny,)


class CheckoutViewSet(viewsets.ViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = (AllowAny,)

    @list_route(methods=['POST',])
    def request_payment(self, request, *args, **kwargs):
        mobile_number = request.data['mobile_number']
        amount = request.data['amount']
        abc = lipisha.request_money(
                account_number="06942",
                mobile_number=mobile_number,
                method="Paybill (M-Pesa)",
                amount=amount,
                currency="KES",
                reference="SoccerGear"
        )
        print(abc)
        return Response(abc)

    @list_route(methods=['POST',])
    def confirm_transaction(self, request, *args, **kwargs):
        transaction = request.data['transaction']

        lipisha = Lipisha(LIPISHA_API_KEY, LIPISHA_API_SIGNATURE, api_environment='test')
        abc = lipisha.confirm_transaction(
                transaction=transaction
        )
        print(abc)
        return Response(abc)
