from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt

from realestate.core.models import User

import json

@csrf_exempt
def register(request):
    """
       Adds a new user with the received fields.
       Authenticates the user after registration.  
    """

    data = json.loads(request.body)
    username = data.get('username')
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    email = data.get('email')
    password = data.get('password')
    

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

    except:
        return HttpResponse(status=500)

    return HttpResponse(status=201)



@csrf_exempt
def login_view(request):
    """
        Authenticates a user with username and 
        password.
    """
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
    """
        Logs the current user (request.user)
        out.
    """


    logout(request)
    return HttpResponse(status=200)