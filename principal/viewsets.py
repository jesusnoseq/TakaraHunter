from rest_framework import viewsets
from rest_framework import filters
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


from rest_framework import viewsets
from models import *
from rest_framework import viewsets, routers
from django.contrib.auth.models import User, Group
from rest_framework import permissions
from filters import *
from serializers import *



class UserAPIView(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        content = {
            'user': unicode(request.user),  # `django.contrib.auth.User` instance.
            'auth': unicode(request.auth),  # None
        }
        return Response(content)

class detalleUsuarioViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Retrieves the suburbs (20 per page).
    GET and OPTIONS allowed.
    """
    model = User

    def get_queryset(self):
        """
        Can filter by region_id, ...
        - using query parameters in the URL.
        """
        queryset = User.objects.all()
        region_id = self.request.QUERY_PARAMS.get('username', None)
        if region_id is not None:
            queryset = queryset.filter(region_id=region_id)
        return queryset


'''
class PurchaseList(generics.ListAPIView)
    serializer_class = PurchaseSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        user = self.request.user
        return Purchase.objects.filter(purchaser=user)'''

#class BusquedasAbiertas(viewsets.ReadOnlyModelViewSet):
#    queryset = 
#    serializer_class = UserSerializer


# ViewSets define the view behavior.
#http://django-rest-framework.org/api-guide/viewsets.html
#http://blog.kevinastone.com/getting-started-with-django-rest-framework-and-angularjs.html
class UserViewSet(viewsets.ModelViewSet):
    model = User
    filter_class = UsernameFilter
    #filter_fields = ('username', 'id')
    serializer_class = UserSerializer
    
    #def get_queryset(self):
    #    return self.request.user.accounts.all()

class GroupViewSet(viewsets.ModelViewSet):
    model = Group

class TesoroViewSet(viewsets.ModelViewSet):
    model = Tesoro


class BusquedaViewSet(viewsets.ModelViewSet):
    model = Busqueda
    filter_class = BusquedaFilter
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)#IsAdminUser
     
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