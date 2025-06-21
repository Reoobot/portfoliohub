from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db import connection
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.apps import apps
from .forms import RegistroForm, VulnerableUserForm
import subprocess
from django.contrib import messages



# ⚠️ LOGIN VULNERABLE a SQL Injection sobre accounts_vulnerableuser
def login_vulnerable(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        print(f"Intento login: {username} / {password}")

        # Obtener el modelo y el nombre real de la tabla en DB
        VulnerableUser = apps.get_model('accounts', 'VulnerableUser')
        table_name = VulnerableUser._meta.db_table

        # Consulta SQL vulnerable, concatenando directamente sin sanitizar
        query = f"SELECT * FROM {table_name} WHERE username = '{username}' AND password = '{password}'"
        print(f"Query ejecutada: {query}")

        with connection.cursor() as cursor:
            cursor.execute(query)
            row = cursor.fetchone()

        print(f"Resultado query: {row}")

        if row:
            print("Login exitoso, redirigiendo...")
            return redirect('/accounts/dashboard_vulnerable/')  # Aquí redirigimos al dashboard sin login
        else:
            print("Credenciales inválidas")
            return HttpResponse("Credenciales inválidas", status=401)

    return render(request, 'accounts/login.html')


# ✅ REGISTRO VULNERABLE (guarda en tabla accounts_vulnerableuser)
def registro_vulnerable(request):
    if request.method == 'POST':
        form = VulnerableUserForm(request.POST)
        if form.is_valid():
            form.save()
            print("Usuario vulnerable registrado")
            return redirect('/accounts/dashboard/')
    else:
        form = VulnerableUserForm()
    return render(request, 'accounts/registro_vulnerable.html', {'form': form})


# ✅ REGISTRO NORMAL (usa modelo auth_user)
def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
        else:
            print(form.errors)  # Verifica qué errores hay
            messages.error(request, "El formulario tiene errores. Revisa los campos.")
    else:
        form = RegistroForm()

    return render(request, 'accounts/registro.html', {'form': form})



# ✅ DASHBOARD protegido (requiere login de Django)
@login_required
def dashboard(request):
    return render(request, 'accounts/dashboard.html')


# ⚠️ DASHBOARD abierto para usuarios del login vulnerable (SIN @login_required)
def dashboard_vulnerable(request):
    return render(request, 'accounts/dashboard.html')

from django.http import HttpResponse
import subprocess

# ⚠️ VISTA VULNERABLE a Command Injection
def command_injection_vulnerable(request):
    cmd = request.GET.get('cmd', '')
    if cmd:
        try:
            output = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, text=True)
        except subprocess.CalledProcessError as e:
            output = e.output
        return HttpResponse(f"<pre>{output}</pre>")
    return HttpResponse("Usa ?cmd=tu_comando para probar")
