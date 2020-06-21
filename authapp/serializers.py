from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Attendance
from .models import UserProfile

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = ['lectureclass','date','present','studentid']



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','password','first_name','last_name','email']


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['studentid','courseenrolled','profilepic']

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['profilepic']
