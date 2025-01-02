from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=50)  #charfield is a fieldtype to set title in database
    rating = models.IntegerField()