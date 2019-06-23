from django.db import models

# Create your models here.
class Room(models.Model):
    name=models.CharField(max_length=15)
class Student(models.Model):
    name=models.CharField(max_length=15)
    sex=models.CharField(max_length=15)
    rid=models.ForeignKey(Room)