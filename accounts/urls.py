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
    path('registro/', views.registro, name='registro'),
    path('login/', views.login_view, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
