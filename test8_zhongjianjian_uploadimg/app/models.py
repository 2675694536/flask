from django.db import models

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=15)
    icon=models.FileField(upload_to='upload')