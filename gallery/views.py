from django.shortcuts import render
from django.http import HttpResponse
from .models import Image

# Create your views here.
def hello(request):
    image_object = Image.objects.all()
    return render(request, 'index.html', {"images":image_object})