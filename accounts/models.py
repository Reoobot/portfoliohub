from django.db import models

# Create your models here.


#class VulnerableUser(models.Model):
#    username = models.CharField(max_length=150)
#    password = models.CharField(max_length=150)

#    def __str__(self):
#        return self.username

#from django.http import HttpResponse
#from accounts.models import VulnerableUser

def crear_usuario_vulnerable(request):
    VulnerableUser.objects.create(username='Hacker', password='admin123')
    return HttpResponse("Usuario vulnerable creado.")
