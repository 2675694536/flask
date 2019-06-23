from django.db import models

# Create your models here.
class User(models.Model):
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
class Book(models.Model):
    bookname=models.CharField(max_length=20)
    author=models.CharField(max_length=20)
class Person(models.Model):
    name = models.CharField(max_length=20)
    sex=models.CharField(max_length=10)
    books=models.ForeignKey(Book)
class People(models.Model):
    name=models.CharField(max_length=15)
    sex=models.CharField(max_length=15)
class Card(models.Model):
    num=models.CharField(max_length=15)
    cid=models.OneToOneField(People)
class Room(models.Model):
    roomname=models.CharField(max_length=15)
class Student(models.Model):
    name=models.CharField(max_length=15)
    sex=models.CharField(max_length=15)
    roomid=models.ForeignKey(Room)
class Good(models.Model):
    name=models.CharField(max_length=15)
    brand=models.CharField(max_length=15)
class Custom(models.Model):
    name=models.CharField(max_length=15)
    sex=models.CharField(max_length=15)
    good=models.ManyToManyField(Good)