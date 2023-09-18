from django.contrib import admin
from django.urls import path
from order.views import (
    OrderCreatelistView,
    OrderRetriveUpdateView,
)

from accounts.views import login_check

urlpatterns = [
    path("admin/", admin.site.urls),
    path("login/<str:username>/<str:password>", login_check),
    path("order/", OrderCreatelistView.as_view()),
    path("order/<str:waybillno>", OrderRetriveUpdateView.as_view()),
]
