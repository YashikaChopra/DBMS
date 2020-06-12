from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ClassLocationSerializer
from .models import ClassLocation

class LocationViewSet(viewsets.ModelViewSet):
    queryset = ClassLocation.objects.all()
    serializer_class = ClassLocationSerializer

# Create your views here.
