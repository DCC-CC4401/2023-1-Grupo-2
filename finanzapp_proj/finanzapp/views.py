from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render

# Create your views here.

#-------------22/04/23----- Manuel y Felipe----->
def login1(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('logeado')  # Redirigir al usuario a la página admin
        else:
           return render(request, 'login.html', {'error_message': 'Nombre de usuario o contraseña incorrectos'})
    else:
        return render(request, 'login.html')

def logeado(request):
    return HttpResponse("logeado")

#-------------22/04/23----- Diego y Gonzalo----->
def register_user(request):
    return render(request,"finanzapp/register_user.html")