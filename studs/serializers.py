from rest_framework import serializers
from studs.models import ClassLocation



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
