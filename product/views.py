from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView
from .models import *


# Create your views here.


class AboutView(TemplateView):
    template_name = 'about.html'


# def about(request):
#     return render(request, 'about.html')


def homepage(request):
    # return HttpResponse('hi')
    products = Vegetables.objects.all()
    context = {'all_vegetables': products}
    return render(request, 'product_list.html', context)  # сначала указыаваем request потом в ковычках указываем путь для html файла


def pomidor(request):
    pomidor_objects = Vegetables.objects.get(id=1)
    description = pomidor_objects.description
    return HttpResponse(description)


def categories_view(request):
    categories = Category.objects.all()
    c = {'categories': categories}  # В ковычках указали контекст его мы используемф html файле чтобы получить данные с БД
    return render(request, 'categories.html', c)

