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



# Create your views here.

def index(response):
    return HttpResponse("<h1>Vinter Capital - vinter.co /app/views.py</h1>")

def view1(response):
    return HttpResponse("<h2>Here goes my app</h2>")