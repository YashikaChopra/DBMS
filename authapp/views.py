from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework import viewsets
from .models import Attendance
from django.contrib.auth import get_user_model
from .serializers import AttendanceSerializer
from .serializers import UserSerializer
from .serializers import UserProfileSerializer
from django.contrib.auth.models import User
from .models import UserProfile
from .serializers import ProfileSerializer
from rest_framework.permissions import IsAuthenticated,AllowAny

class AttendanceViewSet(viewsets.ModelViewSet):
    
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    http_method_names=['post']



class CreateUserViewSet(viewsets.ModelViewSet):
    model=User
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserProfileViewSet(viewsets.ModelViewSet):
    model=UserProfile
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class ProfileViewSet(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer

    def get_queryset(self):
        queryset = UserProfile.objects.all()
        username = self.request.query_params.get('username')

        queryset=queryset.filter(studentid=username)
        return queryset




# Create your views here.


