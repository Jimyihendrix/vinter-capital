from django.shortcuts import render
from django.http import HttpResponse

# imported token-auth, token and api
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view

@api_view(['GET'])
def login(request):
    user = User.objects.get(username='admin')

    token = Token.objects.create(user=user)

    print(token.key)



# Create your views here.

def index(response):
    return HttpResponse("<h1>Vinter Capital - VINTER.CO /config/views.py</h1>")

def view1(response):
    return HttpResponse("<h2>Here goes my app</h2>")
