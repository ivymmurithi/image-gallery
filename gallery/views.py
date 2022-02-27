from django.shortcuts import render
from .models import Image

# Create your views here.
def hello(request):
    if request.method == 'POST':
        if 'results'in request.POST and request.POST.get("results"):
            image_object = Image.objects.filter(category__category_name__icontains=request.POST['results'])
    else:
        image_object = Image.objects.all()
    return render(request, 'index.html', {"images":image_object})
