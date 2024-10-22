from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

from .models import Category


# Create your views here.


def main_menu(request: HttpRequest) -> HttpResponse:
    return render(request, 'recipes/main_menu.html')


#################### CATEGORIES
def category_list(request: HttpRequest) -> HttpResponse:
    categories = Category.objects.all()
    return render(request, 'recipes/category_list.html', {'categories': categories})
