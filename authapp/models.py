from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from studs.models import ClassLocation

class Attendance(models.Model):
    lectureclass=models.ForeignKey(ClassLocation,to_field="NameOfClass",on_delete=models.CASCADE)
    date=models.DateTimeField(default=timezone.now)
    present=models.BooleanField()
    roomno=models.CharField(max_length=100,default="LC1")
    studentid=models.ForeignKey(User,to_field="username",on_delete=models.CASCADE)



    def __str__(self):
        return self.lectureclass


class UserProfile(models.Model):
    studentid=models.ForeignKey(User,to_field="username",on_delete=models.CASCADE)
    profilepic=models.CharField(max_length=1000)
    courseenrolled=models.ManyToManyField(ClassLocation)

    def __str__(self):
        return self.studentid.username




