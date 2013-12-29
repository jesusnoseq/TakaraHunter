from rest_framework import viewsets
from rest_framework import filters
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


from rest_framework import viewsets
from models import *
from rest_framework import viewsets, routers
from django.contrib.auth.models import User, Group
from rest_framework import permissions



# ViewSets define the view behavior.
#http://django-rest-framework.org/api-guide/viewsets.html
#http://blog.kevinastone.com/getting-started-with-django-rest-framework-and-angularjs.html
class UserViewSet(viewsets.ModelViewSet):
    model = User
    
    def get_queryset(self):
        return self.request.user.accounts.all()

class GroupViewSet(viewsets.ModelViewSet):
    model = Group

class TesoroViewSet(viewsets.ModelViewSet):
    model = Tesoro


class BusquedaViewSet(viewsets.ModelViewSet):
    model = Busqueda
    #authentication_classes = (SessionAuthentication, BasicAuthentication)
    #permission_classes = (IsAuthenticated,)#IsAdminUser
     
'''
    
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
'''