from django.db import models

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=15)
    sex=models.CharField(max_length=10)
