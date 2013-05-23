#encoding:utf-8
from django           import forms
from django.forms     import ModelForm
from principal.models import *

class RutaForm(ModelForm):
    class Meta:
        model = Ruta