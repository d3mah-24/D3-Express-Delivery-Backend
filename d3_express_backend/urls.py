from django.contrib import admin
from django.urls import path
from order.views import OrderCreatelistView, updater

from accounts.views import login_check

urlpatterns = [
    path("admin/", admin.site.urls),
    path("login/<str:username>/<str:password>", login_check),
    path("orders/<str:address>", OrderCreatelistView.as_view()),
    path("order", OrderCreatelistView.as_view()),
    path("order/stat/<str:waybillno>/<str:status>/<str:address>", updater),
]
