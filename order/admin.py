from django.contrib import admin

from order.models import Orders


@admin.register(Orders)
class order(admin.ModelAdmin):
    list_display = [
        "id",
        "SenderName",
        "SenderAddress",
        "SenderPhone",
        "receiverName",
        "receiverAddress",
        "receiverPhone",
        "waybillno",
        "price",
        "payment_way",
        "status",
    ]
