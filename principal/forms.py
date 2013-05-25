#encoding:utf-8
from django           import forms
from django.forms     import ModelForm
from django.contrib.auth.models import User
from principal.models import *

class RutaForm(ModelForm):
    class Meta:
        model = Ruta
        

class UserForm(ModelForm):
    class Meta:
        model = User
        exclude=('user','password','is_staff','is_active','is_superuser','last_login','date_joined','groups','user_permissions')
        