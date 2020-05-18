from django.urls import path, include
from django.conf import settings
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET','POST'])
def hello_world(request):
        if request.method == 'POST':
                return Response({"message": "Got some data!", "data": request.data})
        return Response({"message": "Hello, world!"})
    
urlpatterns = [
    path('hello/', hello_world),
]
