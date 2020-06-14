from django.db import models

# Create your models here.
        
class ClassLocation(models.Model):
    NameOfClass = models.CharField(max_length=50)
    #NameOfClass = models.CharField(max_length=50, primary_key=True)
    location = models.CharField(max_length=200)
    #longitude = models.DecimalField(max_digits=9, decimal_places=6)
    #latitude = models.DecimalField(max_digits=9, decimal_places=6)
    radius = models.FloatField()

    def __str__(self):
        return f"{self.NameOfClass}"

class User(models.Model):

    sid = models.CharField(max_length=60)
    name = models.CharField(max_length=60)
    location = models.CharField(max_length=60)
    
    def __str__(self):
        return self.sid


