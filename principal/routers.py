from rest_framework import routers
from rest_framework import viewsets, routers
from django.contrib.auth.models import User, Group
from principal.viewsets import *


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register('tesoros', TesoroViewSet)
#router.register('no-model', viewsets.NoModelViewSet, 'no-model')
