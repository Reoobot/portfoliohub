
# accounts/forms.py
#from django import forms
#from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.models import User

#class RegistroForm(UserCreationForm):
#    email = forms.EmailField(required=True)

#    class Meta:
#        model = User
#        fields = ['username', 'email', 'password1', 'password2']


from django import forms
from .models import VulnerableUser
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class VulnerableUserForm(forms.ModelForm):
    class Meta:
        model = VulnerableUser
        fields = ['username', 'password']

class RegistroForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
