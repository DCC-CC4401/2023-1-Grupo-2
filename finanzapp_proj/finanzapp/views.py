from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from finanzapp.models import User, Transaction
from finanzapp.forms import RegisterUserForm, EditTransactionForm

# Create your views here.

#-------------22/04/23----- Manuel y Felipe----->
def login1(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/main')  # Redirigir al usuario a la página admin
        else:
           return render(request, 'login.html', {'error_message': 'Nombre de usuario o contraseña incorrectos'})
    else:
        return render(request, 'login.html')

def logeado(request):
    if request.user.is_authenticated:
        return HttpResponse("logeado")
    else:
        return HttpResponse("Not logeado")

#-------------22/04/23----- Diego y Gonzalo-----15:30------>

def register_user(request):
    if request.method == 'GET': #Si estamos cargando la página
        form = RegisterUserForm()
        return render(request, "register_user.html", {"register_form": form}) #Mostrar el template

    elif request.method == 'POST': #Si se envía un formulario 
        #Se seleccionan los elementos del formulario con los que se creará el usuario
        nombre = request.POST['nombre']
        contraseña = request.POST['contraseña']
        display = request.POST['display_name']

        #Se crea el nuevo usuario
        user = User.objects.create_user(username=nombre, password=contraseña, display_name=display)

        #Se redirecciona al usuario a main, que será la pagina principal de la app.
        return HttpResponseRedirect('/main')

def logout_view(request): #View para cerrar sesión
    #Si está autenticado, cerramos la sesión
    if request.user.is_authenticated:
        logout(request)
    
    #Redirigimos al inicio de sesión
    return HttpResponseRedirect('/login')

def main(request): #View principal del usuario
    if request.user.is_authenticated:
        return render(request, 'main.html')
    
    #Si no está autenticado, redirigimos al inicio de sesión
    else:
        return HttpResponseRedirect('/login')

#-----------------------------------------------17:19------>

#---------------27/04/2023--------Diego y Gonzalo---------->

def list_transactions(request):
    if request.user.is_authenticated:
        transactions = Transaction.objects.filter(user = request.user)
        return render(request, "listado.html", {"transactions": transactions})
    else:
        return HttpResponseRedirect('/login')


#---------------28/04/2023--------Diego y Gonzalo---------->
def edit_trans(request, id_transaccion):
    if request.user.is_authenticated:
        transaccion= Transaction.objects.filter(id=id_transaccion).first()
        if transaccion.user == request.user:
            form = EditTransactionForm(instance = transaccion)
            return render(request, "edit_trans.html", {"form": form, "transaction": transaccion})
        else:
            return HttpResponseRedirect('/list')
    else:
        return HttpResponseRedirect('/login')


def actualizar_trans(request, id_transaccion):
    if request.user.is_authenticated:
        transaccion = Transaction.objects.filter(id=id_transaccion).first()
        if transaccion.user == request.user:
            form = EditTransactionForm(request.POST, instance = transaccion)
            if form.is_valid():
                form.save()
            return HttpResponseRedirect("/list")
    else:
        return HttpResponseRedirect('/login')
