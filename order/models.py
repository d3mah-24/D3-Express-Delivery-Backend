from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Orders(models.Model):
    SenderName = models.CharField(max_length=30)
    SenderAddress = models.CharField(max_length=30)
    SenderPhone = models.CharField(max_length=30)
    receiverName = models.CharField(max_length=30)
    receiverAddress = models.CharField(max_length=30)
    receiverPhone = models.CharField(max_length=30)
    waybillno = models.CharField(max_length=30, unique=True)
    price = models.CharField(max_length=30)
    payment_way = models.CharField(
        max_length=30,
        default="CASH",
        choices=(
            ("CASH", "CASH"),
            ("COD", "COD"),
        ),
    )
    status = models.CharField(
        max_length=30,
    )
    date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"

    def __str__(self):
        return self.SenderName
