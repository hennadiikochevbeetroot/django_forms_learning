from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.


def main_menu(request: HttpRequest) -> HttpResponse:
    return render(request, 'recipes/main_menu.html')
