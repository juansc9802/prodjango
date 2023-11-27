from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import CustomUserCreationForm, reservaForm
from django.contrib.auth import authenticate, login
from .models import Guarderias, Reserva



# Create your views here.

def home(request):
    return render(request, 'core/home.html')

##Le pide un logeo al usuario para usar esta funcion. Buscando el template login
@login_required 
def products(request):
    guarderia = Guarderias.objects.all()
    context = {
        'products': guarderia,

    }
    return render(request, 'core/products.html', context) ##LE PASAMOS TODA LA INFORMACION DE NUESTRO MODELS GUARDERIAS A EL TEMPLATE EN UNDICCIONARIO, PARA PODER REFERENCIARLO

def exit(request):
    logout(request)
    return redirect('home')

def register(request):
    data = {
        'form': CustomUserCreationForm() ##DICCIONARIO PARA INSTANCIAR EL CUSTOMER USER CREATION FORM PARA LA UTILIDAD DEL FORMULARIO 
    }

    if request.method == 'POST': ##SI es de tipo post toma todos los datos del formulario
        user_creation_form = CustomUserCreationForm(data=request.POST)

        if user_creation_form.is_valid(): ##Revisa que la informaci[on del formulario sea valida
            user_creation_form.save() ##GUarda la informacion

            #user = authenticate(username=user_creation_form.cleaned_data['username'], password=user_creation_form.cleaned_data['password1']) ##Se guarda la informacion a autenticar del formulario creado usando la funcion cleaned data para recibir un campo especifico de la misma funcion
            #login(request, user) ##Si la validacion es correcta hace un login con esa informacion
            return redirect('home')


    return render(request, 'registration/register.html', data)

@login_required 
def reservas_list(request):
    reservas = Reserva.objects.all()
    reservas_pendientes = Reserva.objects.filter(estado='Pendiente')
    reservas_canceladas = Reserva.objects.filter(estado='Cancelado')
    reservas_rechazado = Reserva.objects.filter(estado='Rechazado')
    reservas_aprobado = Reserva.objects.filter(estado='Aprobado')
    return render(request,'core/lista_reservas.html', {'reservas': reservas,'reservas_a': reservas_aprobado, 'reservas_canceladas': reservas_canceladas, 'reservas_p': reservas_pendientes, 'reservas_r': reservas_rechazado})

@login_required 
def hacer_reserva(request, codigo_guarderia):
    
    guarderia = Guarderias.objects.get(codigo=codigo_guarderia)
    if request.method == 'POST':
        form = reservaForm(request.POST)
        if form.is_valid():
            reserva = form.save(commit=False)
            reserva.guarderia = guarderia
            reserva.usuario=request.user
            reserva.save()
            return redirect('detalle_guarderia', codigo_guarderia=int(codigo_guarderia))
    else:
        form = reservaForm()
    
    return render(request, 'core/hacer_reservas.html', {'form':form, 'codig':guarderia})


@login_required
def detalle_guarderia(request, codigo_guarderia):
    guarderia = Guarderias.objects.get(codigo=codigo_guarderia)
    #reservas = Guarderias.reserva_set.all()
    #return render(request, 'core/detalle_guarderia.html', {'guarderia':guarderia, 'reservas': reservas})
    return render(request, 'core/detalle_guarderia.html', {'guarderia':guarderia})

@login_required
def cancelacion(request, id_reserva):
    reserv = Reserva.objects.get(id=id_reserva)
    reserv.estado='Cancelado'
    reserv.save()
    return redirect ('list')