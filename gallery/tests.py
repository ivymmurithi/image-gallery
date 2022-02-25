from django.test import TestCase
from .models import Image,Category,Location
import tempfile

# Create your tests here.
class Image(TestCase):
    def setUp(self):
        self.image1 = Image(name = "ivy's photo",description = "A photo of Ivy",location = 'Africa', category = 'Art')
    def test_instance(self):
        self.assertTrue(isinstance(self.image1,Image))