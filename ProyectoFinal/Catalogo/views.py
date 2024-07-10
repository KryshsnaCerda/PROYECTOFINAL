from django.shortcuts import render, get_object_or_404
from .models import cliente
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.admin.views.decorators import staff_member_required
# Create your views here.

@login_required
def principal(request):
    context={}
    return render(request, 'Catalogo/principal.html', context)


def inicio(request):
    context={}
    return render(request, 'Catalogo/inicio.html', context)

@login_required
def catalogo(request):
    context={}
    return render(request, 'Catalogo/catalogo.html', context)

@login_required
def suscripcion(request):
    context={}
    return render(request, 'Catalogo/suscripcion.html', context)

@login_required
def login(request):
    context={}
    return render(request, 'Catalogo/login.html', context)

@login_required
def registrarse(request):
    context={}
    return render(request, 'Catalogo/registrarse.html', context)


def registrarse(request):
    if request.method == "POST":
        nombre = request.POST.get('nombre')
        contraseña = request.POST.get('contraseña')

        if nombre and contraseña:
            obj = User.objects.create_user(username=nombre, password=contraseña)
            obj.save()
            context = {'mensaje': 'Registrado con éxito'}
            return render(request, 'registrarse.html', context)
        else:
            context = {'mensaje': 'Nombre y/o contraseña no válidos'}
            return render(request, 'registrarse.html', context)
    else:
        context = {'mensaje': ''}
        return render(request, 'registrarse.html', context)

    
def menu(request):
    request.session["usuario"]="kcerda"
    usuario=request.session["usuario"]
    context ={'usuario':usuario}
    return render(request, 'principal.html', context)

@staff_member_required
def admin(request):
    admin = cliente.objects.all()
    context={'admin': admin}
    return render(request, 'admin.html', context) 

@staff_member_required
def annadir_cliente(request):
    if request.method == 'POST':
        correo = request.POST['correo']
        nombre = request.POST['nombre']
        aparterno = request.POST['aparterno']
        amaterno = request.POST['amaterno']
        contraseña = request.POST['contraseña']
        cliente.objects.create(correo=correo, nombre=nombre, aparterno=aparterno, amaterno=amaterno, contraseña=contraseña)
    return render(request, 'Catalogo/annadir_cliente.html')

@staff_member_required
def borrar_cliente(request, pk):
    cliente = get_object_or_404(cliente, correo=pk)
    if request.method == 'POST':
        cliente.delete()
    return render(request, 'Catalogo/borrar_cliente.html')
    return render(request, 'Catalogo/borrar_cliente.html', {'cliente': cliente})
@staff_member_required
def editar_cliente(request, pk):
    cliente = get_object_or_404(cliente, correo=pk)
    if request.method == 'POST':
        cliente.correo = request.POST['correo']
        cliente.nombre = request.POST['nombre']
        cliente.aparterno = request.POST['aparterno']
        cliente.amaterno = request.POST['amaterno']
        cliente.contraseña = request.POST['contraseña']
        cliente.save()
    return render(request, 'Catalogo/editar_cliente.html')