from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt

from realestate.core.models import User


@csrf_exempt
def register(request):
    """
        Registers the user 
    """
    username=request.POST.get('username')
    first_name=request.POST.get('firstName')
    last_name=request.POST.get('lastName')
    email=request.POST.get('email')
    password=request.POST.get('password')


    try:
        User.objects.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password
        )
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)

    except Exception, e:
        print e
        return HttpResponse(status=500)

    return HttpResponse(status=201)

@csrf_exempt
def login_view(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)
    
    if user is not None:
        if user.is_active:
            login(request, user)
        return HttpResponse(status=200)
    else:
        # Returns 401 for failed authentication.
        return HttpResponse(status=401)

@csrf_exempt
def logout_view(request):
    logout(request)
    return HttpResponse(status=200)