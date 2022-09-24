from django.shortcuts import render, HttpResponse
from .models import Vegetables


# Create your views here.
def homepage(request):
    # return HttpResponse('hi')
    products = Vegetables.objects.all()
    context = {'all_vegetables': products}
    return render(request, 'product_list.html', context)  # сначала указыаваем request потом в ковычках указываем путь для html файла


def pomidor(request):
    pomidor_objects = Vegetables.objects.get(id=1)
    description = pomidor_objects.description
    return HttpResponse(description)

