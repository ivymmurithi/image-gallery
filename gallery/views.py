from email import message
from unicodedata import category
from django.shortcuts import render
from django.http import HttpResponse
from .models import Image

# Create your views here.
def hello(request):
    if request.method == 'POST':
        if 'results'in request.POST and request.POST.get("results"):
            image_object = Image.objects.filter(category__category_name__icontains=request.POST['results'])
            # message = f"{}"
    else:
        image_object = Image.objects.all()
    return render(request, 'index.html', {"images":image_object})
