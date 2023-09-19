from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate,login

User = get_user_model()

from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def login_check(req, username, password):
    if req.method == "GET":
        print(req.POST)
        a = authenticate(username=username, password=password)

        print(username, password, a)
        if a is not None:
            login(req, a)
            
            return HttpResponse(a.address,
                status=200,
            )
    return HttpResponse( status=404)
