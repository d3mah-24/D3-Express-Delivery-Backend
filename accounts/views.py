from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate

User = get_user_model()


def login_check(req):
    if req.method == "POST":
        username = req.POST.get("username")
        password = req.POST.get("password")
        a = authenticate(username=username, password=password)
        print(username, password)
        if a is not None:
            return HttpResponse(
                status=200,
            )
    return HttpResponse(status=404)
