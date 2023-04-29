from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from finanzapp.models import User, Transaction
from django.utils import timezone

# Create your views here.

#-------------22/04/23----- Manuel y Felipe----->
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  # Redirigir al usuario a la página admin
        else:
           return render(request, 'login.html', {'error_message': 'Nombre de usuario o contraseña incorrectos'})
    else:
        return render(request, 'login.html')

#-------------22/04/23----- Diego y Gonzalo----->

def register(request):
    if request.method == 'GET': #Si estamos cargando la página
        return render(request, "register_user.html") #Mostrar el template

    elif request.method == 'POST': #Si estamos recibiendo el form de registro
        #Tomar los elementos del formulario que vienen en request.POST
        nombre = request.POST['nombre']
        contraseña = request.POST['contraseña']
        display = request.POST['display_name']

        #Crear el nuevo usuario
        user = User.objects.create_user(username=nombre, password=contraseña, display_name=display)
        user.save()
        # Loggear al usuario nuevo
        login(request, user)
        #Redireccionar la página /tareas
        return redirect('index')
    
def index(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return render(request, 'index.html', {'today': timezone.now().strftime("%Y-%m-%d")})
        else:
            return redirect('login')
    elif request.method == "POST":
        user = request.user
        type = request.POST['type']
        description = request.POST['description']
        amount = request.POST['amount']
        date = request.POST['date']
        transaction = Transaction.objects.create(user=user, type=type, description=description, amount=amount, date=date)
        transaction.save()
        return redirect('index')
    