from django.db import models

# Create your models here.
class userdata(models.Model):
    name=models.CharField(max_length=50)
    phone=models.IntegerField()
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=50)