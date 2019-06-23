from django.db import models

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    age=models.IntegerField(default=18)
    is_delete=models.BooleanField(default=0)
    class Meta:
        db_table='user'