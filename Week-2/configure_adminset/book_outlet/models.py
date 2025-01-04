from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=50)  #charfield is a fieldtype to set title in database
    rating = models.IntegerField( validators=[MinValueValidator(1), MaxValueValidator(5)])
    author = models.CharField(null=True, max_length=100)
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(default="", null=False, blank=True, db_index=True)

    def get_absolute_url(self):
        return reverse("book-detail", args= [self.slug])
    
    def __str__(self):
        return f"{self.title} ({self.rating})"