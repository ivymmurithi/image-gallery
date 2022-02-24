from unicodedata import category
from django.db import models

# Create your models here.
class Image(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    gallery_image = models.ImageField(upload_to = 'galleries/', blank=False)


class Location(models.Model):
    location_name = models.CharField(max_length=30)

class Category(models.Model):
    category_name = models.CharField(max_length=30)