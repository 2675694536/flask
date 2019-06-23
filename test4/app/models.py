from django.db import models

# Create your models here.
class Person(models.Model):
    name=models.CharField(max_length=20)
    sex=models.CharField(max_length=20)
    age=models.CharField(max_length=10)
class Card(models.Model):
    num=models.CharField(max_length=18)
    pid=models.OneToOneField(Person)