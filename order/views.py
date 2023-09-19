from rest_framework import generics
from order.models import Orders
from order.serializer import OrderSerializer
from django.db.models import Q


class OrderCreatelistView(generics.ListCreateAPIView):
    lookup_field = "waybillno"
    serializer_class = OrderSerializer

    def get_queryset(self):
        address = self.kwargs.get("address")
        queryset = Orders.objects.filter(
            Q(receiverAddress=address) | Q(receiverAddress=address)
        )
        return queryset


class OrderRetriveUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrderSerializer
    lookup_field = "waybillno"
