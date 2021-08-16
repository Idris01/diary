from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import viewsets
from .serializer import TodoSerializer
import json
from .models import Todo

# Create your views here.

def index(request):
    if request.method=="GET":
        data={"msg":"Hello World"}
        return JsonResponse(data, safe=False)

class TodoView(viewsets.ModelViewSet):
    serializer_class=TodoSerializer
    queryset=Todo.objects.all()
