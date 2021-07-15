from django.shortcuts import render
from django.http import HttpResponse

# imported token-auth, token and api
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
# imported auth hasher
from django.contrib.auth.hashers import check_password
# response
from rest_framework.response import Response

@api_view(['POST'])
def login(request):

    username = request.POST.get('username')
    password = request.POST.get('password')
    

    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return Response("Usuario invalido")

    pwd_valid = check_password(password, user.password)

    if not pwd_valid:
        return Response("Contraseña Invalida")

    token = Token.objects.create(user=user)

    print(token.key)
    return Response(token.key)



# Create your views here.

def index(response):
    return HttpResponse("<h1>Vinter Capital - VINTER.CO /config/views.py</h1>")

def view1(response):
    return HttpResponse("<h2>Here goes my app</h2>")
