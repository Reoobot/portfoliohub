#from django.urls import path
#from . import views

#urlpatterns = [
#    path('', views.index, name='portfolios index'),
    # otras rutas de portfolios
#]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.portfolio_list, name='portfolios index'),
]


