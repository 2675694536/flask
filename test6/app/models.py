from django.db import models

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=15)
    password=models.CharField(max_length=15)
class Book(models.Model):
    name=models.CharField(max_length=15)
    author=models.CharField(max_length=15)
class Person(models.Model):
    name=models.CharField(max_length=15)
    sex=models.CharField(max_length=15)
    books=models.ForeignKey(Book)