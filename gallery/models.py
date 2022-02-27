from django.db import models
import pyperclip

# Create your models here.
class Image(models.Model):
    """
    Image models for database
    """
    name = models.CharField(max_length=30)
    description = models.TextField()
    gallery_image = models.ImageField(upload_to = 'galleries/')
    location = models.ForeignKey('Location', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    
    def __str__(self):
        """
        Represents the class objects as a string. Makes its easy to 
        read outputs for all the members of the class.
        """
        return self.name

    def save_image(self):
        """
        Save category objects
        """
        self.save()

    def delete_image(self):
        """
        Delete category objects
        """
        self.delete()

class Location(models.Model):
    """
    Location model for database
    """
    location_name = models.CharField(max_length=30)

    def __str__(self) -> str:
        """
        Represents the class objects as a string. Makes its easy to 
        read outputs for all the members of the class.
        """
        return self.location_name

    def save_location(self):
        """
        Save category objects
        """
        self.save()

    def delete_location(self):
        """
        Delete category objects
        """
        self.delete()

class Category(models.Model):
    """
    Category model for database
    """
    category_name = models.CharField(max_length=30)

    def __str__(self) -> str:
        """
        Represents the class objects as a string. Makes its easy to 
        read outputs for all the members of the class.
        """
        return self.category_name

    def save_category(self):
        """
        Save category objects
        """
        self.save()

    def delete_category(self):
        """
        Delete category objects
        """
        self.delete()