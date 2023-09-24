from django.http import Http404, HttpResponse
from rest_framework import generics
from order.models import Orders
from order.serializer import OrderSerializer
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt


class OrderCreatelistView(generics.ListCreateAPIView):
    lookup_field = "waybillno"
    serializer_class = OrderSerializer

    def get_queryset(self):
        address = self.kwargs.get("address")
        queryset = Orders.objects.filter(
            Q(SenderAddress=address) | Q(receiverAddress=address)
        )
        return queryset


@csrf_exempt
def updater(req, waybillno, status):
    order = Orders.objects.get(waybillno=waybillno)
    order.status = status
    order.save()
    return HttpResponse(
        "Done",
        status=200,
    )


@csrf_exempt
def update_stat(req, waybillno, curr_location):
    order = Orders.objects.get(waybillno=waybillno)
    order.curr_location = curr_location
    order.save()
    return HttpResponse(
        "Done",
        status=200,
    )
