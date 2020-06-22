from django.db import models

# Create your models here.
        
class ClassLocation(models.Model):
    NameOfClass = models.CharField(max_length=50)
    location = models.CharField(max_length=200)
    radius = models.FloatField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.NameOfClass}"


