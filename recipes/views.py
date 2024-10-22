from django.http import HttpRequest, HttpResponse, HttpResponseBadRequest
from django.shortcuts import get_object_or_404, redirect, render

from .forms import CategoryForm
from .models import Category


# Create your views here.


def main_menu(request: HttpRequest) -> HttpResponse:
    return render(request, 'recipes/main_menu.html')


#################### CATEGORIES
def category_list(request: HttpRequest) -> HttpResponse:
    categories = Category.objects.all()
    return render(request, 'recipes/category_list.html', {'categories': categories})


def category_create(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        # Submit button pressed
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('recipes:category_list')
        else:
            return HttpResponseBadRequest('Form is incorrectly filled')
    else:
        # Empty form to fill
        form = CategoryForm()

    return render(request, 'recipes/category_form.html', {'form': form})


def category_edit(request: HttpRequest, pk: int) -> HttpResponse:
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        # Submit button pressed
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('recipes:category_list')
        else:
            return HttpResponseBadRequest('Form is incorrectly filled')
    else:
        # Existing record form to change
        form = CategoryForm(instance=category)

    return render(request, 'recipes/category_form.html', {'form': form})
