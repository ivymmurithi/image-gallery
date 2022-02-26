from unicodedata import category
from django.db import models

# Create your models here.
class Image(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    gallery_image = models.ImageField(upload_to = 'galleries/')
    location = models.ForeignKey('Location', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

    def save_image(self):
        self.save()

class Location(models.Model):
    location_name = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.location_name

    def save_location(self):
        self.save()

class Category(models.Model):
    category_name = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.category_name

    def save_category(self):
        self.save()