from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import LoginForm, CustomUserCreationForm ,PresupuestoForm, ItemFormSet
from .models import Presupuesto

def user_is_ingeniero(user):
    return user.is_authenticated and user.role == 'ingeniero'

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def home_view(request):
    if not request.user.is_authenticated:
        return redirect('inicio')
    return render(request, 'home.html')

@login_required
@user_passes_test(user_is_ingeniero)
def crear_usuario_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'crear_usuario.html', {'form': form})

# Create your views here.
def inicio_publico(request):
    return render(request, 'inicio.html')

# vista del presupuesto protegida paea el ingeniero
@login_required
@user_passes_test(user_is_ingeniero)
def crear_presupuesto(request):
    if request.method == 'POST':
        form = PresupuestoForm(request.POST)
        formset = ItemFormSet(request.POST)

        if form.is_valid() and formset.is_valid():
            presupuesto = form.save(commit=False)
            presupuesto.creado_por = request.user
            presupuesto.save()
            formset.instance = presupuesto
            formset.save()
            return redirect('lista_presupuestos.html')  # Cambia por tu ruta real
    else:
        form = PresupuestoForm()
        formset = ItemFormSet()

    return render(request, 'crear_presupuesto.html', {
        'form': form,
        'formset': formset
    })
    
    #vista para listar presupuestos
@login_required
@user_passes_test(user_is_ingeniero)
def lista_presupuestos(request):
    presupuestos = Presupuesto.objects.filter(creado_por=request.user)
    return render(request, 'lista_presupuestos', {
        'presupuestos': presupuestos
    })