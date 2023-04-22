from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def inicio_sesion(request, usuario , clave):

    return HttpResponse("Ingrese aquí:")
