from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Attendance(models.Model):
    lectureclass=models.CharField(max_length=50)
    date=models.DateTimeField(default=timezone.now)
    present=models.BooleanField()
    studentid=models.ForeignKey(User,to_field="username",on_delete=models.CASCADE)


    def __str__(self):
        return self.lectureclass


class UserProfile(models.Model):
    studentid=models.ForeignKey(User,to_field="username",on_delete=models.CASCADE)
    courseenrolled=models.CharField(max_length=50)
    profilepic=models.CharField(max_length=1000)

    def __str__(self):
        return self.courseenrolled




