from rest_framework import serializers
from studs.models import ClassLocation
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('sid','name','location')

class ClassLocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = ClassLocation
        fields = '__all__'
        #fields = ('latitude', 'longitude')
        #fields = ['location']

class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = ClassLocation
        fields = ('location', 'radius')
        #fields = '__all__'
        #fields = ('latitude', 'longitude')
        #fields = ['location']
