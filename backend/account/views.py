from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def index(request):
    if request.method=="GET":
        data={"msg":"Hello World"}
        return JsonResponse(data, safe=False)
