from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate, login
# Create your views here.

@api_view(['POST'])
def register(request):
    if request.method == 'POST':
        pass
        
