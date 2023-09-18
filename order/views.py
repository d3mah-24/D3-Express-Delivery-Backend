from rest_framework import generics
from order.models import Orders
from order.serializer import OrderSerializer


class OrderCreatelistView(generics.ListCreateAPIView):
    queryset = Orders.objects.all()
    lookup_field = "waybillno"
    serializer_class = OrderSerializer


class OrderRetriveUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrderSerializer
    lookup_field = "waybillno"
