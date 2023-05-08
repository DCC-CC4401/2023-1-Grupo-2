from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from finanzapp.models import User, Transaction, Category
from finanzapp.forms import RegisterUserForm, EditTransactionForm
from django.utils import timezone
from django.db.models import Sum
# Create your views here.

#-------------22/04/23----- Manuel y Felipe----->
def login_1(request):
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
        form = RegisterUserForm()
        return render(request, "register_user.html", {"register_form": form}) #Mostrar el template

    elif request.method == 'POST': #Si se envía un formulario 
        #Se seleccionan los elementos del formulario con los que se creará el usuario
        nombre = request.POST['nombre']
        contraseña = request.POST['contraseña']
        display = request.POST['display_name']
        #Se crea el nuevo usuario
        user = User.objects.create_user(username=nombre, password=contraseña, display_name=display)
        user.save()
        # Se crea la categoría ninguna por default:
        category = Category(name="ninguna", budget=0, user=user)
        category.save()
        #Se redirecciona al usuario a index, que será la pagina principal de la app.
        return redirect('index')

def logout_view(request): #View para cerrar sesión
    #Si está autenticado, cerramos la sesión
    if request.user.is_authenticated:
        logout(request)
    
    #Redirigimos al inicio de sesión
    return redirect('login')


#-----------------------------------------------12:00------>

#---------------29/04/2023--------Felipe, Lucas y Manuel---------->
#funcion auxiliar que devuelve el saldo disponible de cierto usuario
def saldo_disponible(user_id):
    #esto devuelve el total de montos de transacciones etiquetas como depositos
    depositos = Transaction.objects.filter(user_id=user_id, type='deposit').aggregate(Sum('amount'))['amount__sum'] or 0
    #esto devuelve el total de montos de transacciones etiquetas como gastos
    gastos = Transaction.objects.filter(user_id=user_id, type='spend').aggregate(Sum('amount'))['amount__sum'] or 0
    saldo = depositos - gastos
    #devuelve la resta entre depositos y gastos
    return saldo

def index(request):
    # Cuando se carga la página
    if request.method == 'GET':
        #Por motivos de seguridad un usuario no autenticado no puede acceder a el listado
        if request.user.is_authenticated:
            # Se recupera el usuario
            user_id= request.user
            #se calcula el saldo disponible para el usuario ya logeado
            saldo = saldo_disponible(user_id)
            # Se cargan todas las catehorias del usuario
            categories = Category.objects.filter(user=user_id)
            #se guarda como diccionario
            context = {'saldo': saldo, 'categories': categories, 'today': timezone.now().strftime("%Y-%m-%d")}
            # Se renderiza la página
            return render(request, 'index.html', context)
        # Si el usuario no está autenticado, se redirecciona al login
        else:
            return redirect('login')
    # Cuando se envía el formulario
    elif request.method == "POST":
        # Se recupera el usuario
        user = request.user
        # Se recuperan los campos del formulario
        type = request.POST['type']
        description = request.POST['description']
        amount = request.POST['amount']
        date = request.POST['date']
        category = request.POST['category']
        cat = Category.objects.filter(user=user, name=category).first()
        # Se crea un objeto transacción
        transaction = Transaction.objects.create(user=user, type=type, description=description, amount=amount, date=date, category=cat)
        transaction.save()
        # Se vuelve a la misma página
        return redirect('index')

#-----------------------------------------------17:19------>

#---------------27/04/2023--------Diego y Gonzalo---------->

#Función que lista las transacciones de un usuario
def list_transactions(request):
    #Si el usuario está autenticado, buscamos sus transacciones
    if request.user.is_authenticated:
        transactions = Transaction.objects.filter(user = request.user)
        #Le pasamos las transacciones al formulario
        return render(request, "listado.html", {"transactions": transactions})
    #Si no está autenticado, lo mandamos a login
    else:
        return redirect('login')


#---------------28/04/2023--------Diego y Gonzalo---------->
#Función que edita el registro de una transacción
def edit_trans(request, id_transaccion):
    #Por motivos de seguridad un usuario no autenticado no puede acceder a el listado
    if request.user.is_authenticated:
        transaccion= Transaction.objects.filter(id=id_transaccion).first()
        #El usuario asociado a la transacción debe ser el mismo que quiere realizar el edit, 
        #de lo contrario, podría editar el de otra persona
        if transaccion.user == request.user: 
            #obtenemos el formulario haciendo llamada a funcion de forms.py
            form = EditTransactionForm(instance = transaccion)
            #entregamos el formulario editado con su id de transacción para ser llamado en actualizar
            return render(request, "edit_trans.html", {"form": form, "transaction": transaccion})
        else:
            return redirect('list')
    #Si no está autenticado, lo mandamos a login
    else:
        return redirect('login')

#Función que actualiza una transacción en la base de datos
def actualizar_trans(request, id_transaccion):
    if request.user.is_authenticated: #Revisamos si el usuario está autenticado
        #Obtenemos la transacción con el id buscado
        transaccion = Transaction.objects.filter(id=id_transaccion).first()
        #El usuario asociado a la transacción debe ser el mismo que quiere realizar el edit, 
        #de lo contrario, podría editar el de otra persona
        if transaccion.user == request.user:
            form = EditTransactionForm(request.POST, instance = transaccion)
            if form.is_valid(): #Si los cambios cumplen las restricciones de los campos, guardamos los cambios
                form.save()
        #Redirigimos hacia el listado de transacciones
        return redirect('list')
    #Si no está autenticado, lo mandamos a login
    else:
        return redirect('login')

        
#Funcion que elimina registros de transacciones
def delete_trans(request,id_transaccion):
    if request.user.is_authenticated:
        transaccion = Transaction.objects.filter(id=id_transaccion).first()
        #El usuario asociado a la transacción debe ser el mismo que quiere realizar el edit, 
        #de lo contrario, podría eliminar el de otra persona
        if transaccion.user == request.user:
            #Eliminamos y redirigimos al listado de transacciones
            transaccion.delete()
        return redirect('list')
    #Si no está autenticado, lo mandamos a login
    else:
        return redirect('login')
