from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def getRoutes(request):
    routes = [
        '/api/weather/',
        '/api/weather/<location>',
    ]

    return JsonResponse(routes, safe=False)