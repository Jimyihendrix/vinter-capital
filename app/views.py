from django.shortcuts import render
from django.http import HttpResponse


# views and response
from rest_framework.views import APIView
from rest_framework.response import Response

#permission
from rest_framework.permissions import IsAuthenticated




# views and responnse
class HelloView(APIView):
    #permission
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)



#python request token     user: jimyihendrix and email: jimyihendrix@gmail.com
#import requests

#url = 'http://127.0.0.1:8000/hello/'
#headers = {'Authorization': 'Token 2a021aed7b115975b8ce91090e82c1bf7c1d35dd'}
#r = requests.get(url, headers=headers)




# Create your views here.

def index(response):
    return HttpResponse("<h1>Vinter Capital - vinter.co /app/views.py</h1>")

def view1(response):
    return HttpResponse("<h2>Here goes my app</h2>")