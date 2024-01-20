from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class CuisineType(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

class Restaurant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    place = models.CharField(max_length=255)
    cuisine = models.ForeignKey(CuisineType, on_delete=models.PROTECT)
    
    def __str__(self):
        return self.name
    