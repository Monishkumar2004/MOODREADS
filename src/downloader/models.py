from django.db import models

# Create your models here.

class Book_data(models.Model):
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=200)
    image = models.ImageField()