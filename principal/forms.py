#encoding:utf-8
from django           import forms
from django.forms     import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from principal.models import *

class RutaForm(ModelForm):
    class Meta:
        model = Ruta
        

class UserForm(ModelForm):
    class Meta:
        model = User
        exclude=('user','password','is_staff','is_active','is_superuser','last_login','date_joined','groups','user_permissions')
        
class PerfilCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user