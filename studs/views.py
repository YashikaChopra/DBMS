from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ClassLocationSerializer
from .models import ClassLocation
from .models import User
from .serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset=User.objects.all().order_by('sid')
    serializer_class=UserSerializer

class LocationViewSet(viewsets.ModelViewSet):
    queryset = ClassLocation.objects.all()
    serializer_class = ClassLocationSerializer

# Create your views here.
