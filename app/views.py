from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(response):
    return HttpResponse("<h1>Vinter Capital - App Updated</h1>")

def view1(response):
    return HttpResponse("<h2>Here goes my app</h2>")


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated  


class HelloView(APIView):
    permission_classes = (IsAuthenticated,)             

    def get(self, request):
        content = {'message': 'Hello, Hakan, how are you doing!?'}
        return Response(content)


#Generated token c1560085c045489964d3c572e93e1ceb089a1c16 for user jimyihendrix


