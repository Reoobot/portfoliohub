#from django.shortcuts import render

# Create your views here.


#from django.http import HttpResponse

#def index(request):
#    return HttpResponse("¡Hola desde portfolios index Account!")

# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from .forms import RegistroForm

# Vista de registro
def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Inicia sesión automáticamente
            return redirect('dashboard')  # Redirige al dashboard
    else:
        form = RegistroForm()
    return render(request, 'accounts/registro.html', {'form': form})

# Vista de login
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or '/accounts/dashboard/')
#return redirect('dashboard')  # Redirige al dashboard si el login es exitoso
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

# Vista protegida del panel de usuario
@login_required
def dashboard(request):
    return render(request, 'accounts/dashboard.html')
