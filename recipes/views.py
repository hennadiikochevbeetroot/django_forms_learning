from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from .forms import CategoryForm, IngredientForm
from .models import Category, Ingredient


######################### MAIN MENU
def main_menu(request: HttpRequest) -> HttpResponse:
    return render(request, 'recipes/main_menu.html')


######################### CATEGORIES

# CREATE
def category_create(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('recipes:category_list')
    else:
        form = CategoryForm()
    return render(request, 'recipes/category_form.html', {'form': form})


# READ - list
def category_list(request: HttpRequest) -> HttpResponse:
    categories = Category.objects.all()
    return render(request, 'recipes/category_list.html', {'categories': categories})


# UPDATE
def category_update(request: HttpRequest, pk: int) -> HttpResponse:
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('recipes:category_list')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'recipes/category_form.html', {'form': form})


# DELETE
def category_delete(request: HttpRequest, pk: int) -> HttpResponse:
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('recipes:category_list')
    return render(request, 'recipes/category_confirm_delete.html', {'category': category})


######################### INGREDIENTS


# CREATE
def ingredient_create(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = IngredientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('recipes:ingredient_list')
    else:
        form = IngredientForm()
    return render(request, 'recipes/ingredient_form.html', {'form': form})


# READ - list
def ingredient_list(request: HttpRequest) -> HttpResponse:
    ingredients = Ingredient.objects.all()
    return render(request, 'recipes/ingredient_list.html', {'ingredients': ingredients})


# UPDATE
def ingredient_update(request: HttpRequest, pk: int) -> HttpResponse:
    ingredient = get_object_or_404(Ingredient, pk=pk)
    if request.method == 'POST':
        form = IngredientForm(request.POST, instance=ingredient)
        if form.is_valid():
            form.save()
            return redirect('recipes:ingredient_list')
    else:
        form = IngredientForm(instance=ingredient)
    return render(request, 'recipes/ingredient_form.html', {'form': form})


def ingredient_delete(request: HttpRequest, pk: int) -> HttpResponse:
    ingredient = get_object_or_404(Ingredient, pk=pk)
    if request.method == 'POST':
        ingredient.delete()
        return redirect('recipes:ingredient_list')
    return render(request, 'recipes/ingredient_confirm_delete.html', {'ingredient': ingredient})
