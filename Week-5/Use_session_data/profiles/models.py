from django.db import models

# Create your models here.

class UserProfile(models.Model):
    image = models.ImageField(upload_to= "images")  #it uploads the image to a folder in root dir and to images