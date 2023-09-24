from django.contrib import admin
from django.urls import path
from order.views import OrderCreatelistView, update_stat, updater

from accounts.views import login_check

urlpatterns = [
    path("admin/", admin.site.urls),
    path("login/<str:username>/<str:password>", login_check),
    path("orders/<str:address>", OrderCreatelistView.as_view()),
    path("order", OrderCreatelistView.as_view()),
    path("order/stat/<str:waybillno>/<str:status>", updater),
    path("order/loc/<str:waybillno>/<str:status>", update_stat),
]
