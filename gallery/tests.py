from django.test import TestCase
from .models import Image,Category,Location


# Create your tests here.
class ImageTestClass(TestCase):

    """
    Setup for image class
    """

    def setUp(self):
        self.location1 = Location(location_name = "Africa")
        self.location1.save_location()
        self.category1 = Category(category_name = 'Art')
        self.category1.save_category()
        self.image1 = Image(name = "ivy's photo",description = "A photo of Ivy", location = self.location1, category = self.category1)

    def test_instance(self):
        """
        Test if Image is instantiating right
        """
        self.assertTrue(isinstance(self.image1,Image))

    def test_save_method(self):
        """
        Test save method
        """
        self.image1.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)

    def test_delete_method(self):
        """
        Test delete method
        """
        self.image1.save_image()
        self.image1.delete_image()
        images = Image.objects.all()
        self.assertTrue(len(images) - 1)

class LocationTestClass(TestCase):

    """
    Setup for Location class
    """
    def setUp(self):
        self.location1 = Location(location_name = "Africa")

    def test_instance(self):
        """
        Test if Location is instantiating right
        """
        self.assertTrue(isinstance(self.location1,Location))

    def test_save_method(self):
        """
        Test save method
        """
        self.location1.save_location()

    def test_delete_method(self):
        """
        Test delete method
        """
        self.location1.save_location()
        self.location1.delete_location()
        location = Location.objects.all()
        self.assertTrue(len(location) - 1)

class CategoryTestClass(TestCase):
    """
    Setup for Category class
    """
    def setUp(self):
        self.category1 = Category(category_name = 'Art')

    def test_instance(self):
        """
        Test if category is instantiating right
        """
        self.assertTrue(isinstance(self.category1,Category))

    def test_save_method(self):
        """
        Test save method
        """
        self.category1.save_category()

    def test_delete_method(self):
        """
        Test delete method
        """
        self.category1.save_category()
        self.category1.delete_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) - 1)

    def tearDown(self):
        """
        Tear down method for deleting all instances of the models
        from the database after each test
        """
        Image.objects.all().delete()
        Location.objects.all().delete()
        Category.objects.all().delete()
  