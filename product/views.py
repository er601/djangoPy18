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
    return render(request, 'product/list.html', context)  # сначала указыаваем request потом в ковычках указываем путь для html файла


def vegetable_detail(request, id):
    vegetable = Vegetables.objects.get(id=id)
    context = {'vegetable': vegetable}
    return render(request, 'product/vegetable_info.html', context)


def pomidor(request):
    pomidor_objects = Vegetables.objects.get(id=1)
    description = pomidor_objects.description
    return HttpResponse(description)


def categories_view(request):
    categories = Category.objects.all()
    c = {'categories': categories}  # В ковычках указали контекст его мы используемф html файле чтобы получить данные с БД
    return render(request, 'product/categories.html', c)


def category_detail(request, id):
    # SELECT * FROM Vegetables WHERE category = (SELECT id FROM Category WHERE id = id)
    category_object = Category.objects.get(id=id)
    vegetables_list = Vegetables.objects.filter(category=category_object)
    context = {'all_vegetables': vegetables_list}
    return render(request, 'product/list.html', context)

