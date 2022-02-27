from email import message
from django.shortcuts import render
from .models import Image

# Create your views here.
def hello(request):
    if request.method == 'POST':
        if 'results'in request.POST and request.POST.get("results"):
            """
            Get user input
            """
            search_query = request.POST['results']

            """
            Enable Search for both category and location
            """
            filter_category = {
                "category__category_name__icontains": search_query, 
            }
            filter_location = {
                "location__location_name__icontains": search_query,
            }
            image_object = Image.objects.filter(**filter_location)
            if len(image_object) < 1:
                image_object = Image.objects.filter(**filter_category)
            if len(image_object) == 0:
                message('Search term does not exist')
    else:
        image_object = Image.objects.all()
    return render(request, 'index.html', {"images":image_object})
