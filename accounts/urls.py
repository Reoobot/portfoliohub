#from django.contrib import admin
#from django.urls import path, include

#urlpatterns = [
#    path('admin/', admin.site.urls),
#    path('accounts/', include('accounts.urls')),  # Esto incluye las rutas de la app accounts
#]


#from django.urls import path
#from . import views

#urlpatterns = [
#    path('', views.index, name='index'),
    # otras rutas aquí
#]


# accounts/urls.py
from django.urls import path
from . import views

urlpatterns = [
    #path('registro/', views.registro, name='registro'),
    #path('login/', views.login_view, name='login'),
    path('registro/register/', views.registro_vulnerable, name='registro_vulnerable'),
    path('login/create/', views.login_vulnerable, name='login_vulnerable'),
    path('dashboard_vulnerable/', views.dashboard_vulnerable, name='dashboard_vulnerable'),
    path('accounts/dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('registro/', views.registro, name='registro'),
    path('command_injection/', views.command_injection_vulnerable, name='command_injection'),
]
