from django.db import models
from datetime import datetime

# Create your models here.
        
class ClassLocation(models.Model):
    NameOfClass = models.CharField(max_length=50,unique=True)
    latitude = models.CharField(max_length=200,default="1N")
    longitude= models.CharField(max_length=200,default="1N")
    radius = models.FloatField()
    roomno = models.CharField(max_length=50,default="LC1")
    start_time = models.TimeField(default=datetime.now())
    end_time = models.TimeField(default=datetime.now())

    def __str__(self):
        return f"{self.NameOfClass}"


