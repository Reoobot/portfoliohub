#from django.urls import path
#from . import views

#urlpatterns = [
#    path('', views.index, name='jobs_index'),
    # otras rutas de jobs
#]


from django.urls import path
from . import views

urlpatterns = [
    path('', views.job_list, name='jobs index'),
]
