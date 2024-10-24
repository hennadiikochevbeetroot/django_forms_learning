from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from .forms import CategoryForm, IngredientForm, RecipeForm
from .models import Category, Ingredient, Recipe


######################### MAIN MENU
def main_menu(request: HttpRequest) -> HttpResponse:
    return render(request, 'recipes/main_menu.html')


######################### CATEGORIES

# CREATE
@login_required
def category_create(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.user = request.user
            category.save()
            return redirect('recipes:category_list')
    else:
        form = CategoryForm()
    return render(request, 'recipes/category_form.html', {'form': form})


# READ - list
@login_required
def category_list(request: HttpRequest) -> HttpResponse:
    categories = Category.objects.filter(user=request.user)
    return render(request, 'recipes/category_list.html', {'categories': categories})


# UPDATE
@login_required
def category_update(request: HttpRequest, pk: int) -> HttpResponse:
    category = get_object_or_404(Category, pk=pk, user=request.user)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('recipes:category_list')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'recipes/category_form.html', {'form': form})


# DELETE
@login_required
def category_delete(request: HttpRequest, pk: int) -> HttpResponse:
    category = get_object_or_404(Category, pk=pk, user=request.user)
    if request.method == 'POST':
        category.delete()
        return redirect('recipes:category_list')
    return render(request, 'recipes/category_confirm_delete.html', {'category': category})


######################### INGREDIENTS


# CREATE
@login_required
def ingredient_create(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = IngredientForm(request.POST)
        if form.is_valid():
            ingredient = form.save(commit=False)
            ingredient.user = request.user
            ingredient.save()
            return redirect('recipes:ingredient_list')
    else:
        form = IngredientForm()
    return render(request, 'recipes/ingredient_form.html', {'form': form})


# READ - list
@login_required
def ingredient_list(request: HttpRequest) -> HttpResponse:
    user_groups_ids = request.user.groups.values('id')
    ingredients = Ingredient.objects.filter(user__groups__in=user_groups_ids)
    # select * from ingredient
    # join user on ingredient.user_id = user.id
    # join user_groups on user.id = user_groups.user_id
    # join group on user_groups.group_id = group.id
    # where group.id in (
    #    select id from group
    #    join user_groups on group.id = user_groups.group_id
    #    join user on user_groups.user_id = user.id
    #    where user.id = {request.user.id}
    # )
    return render(request, 'recipes/ingredient_list.html', {'ingredients': ingredients})


# UPDATE
@login_required
def ingredient_update(request: HttpRequest, pk: int) -> HttpResponse:
    ingredient = get_object_or_404(Ingredient, pk=pk, user=request.user)
    if request.method == 'POST':
        form = IngredientForm(request.POST, instance=ingredient)
        if form.is_valid():
            form.save()
            return redirect('recipes:ingredient_list')
    else:
        form = IngredientForm(instance=ingredient)
    return render(request, 'recipes/ingredient_form.html', {'form': form})


@login_required
def ingredient_delete(request: HttpRequest, pk: int) -> HttpResponse:
    ingredient = get_object_or_404(Ingredient, pk=pk, user=request.user)
    if request.method == 'POST':
        ingredient.delete()
        return redirect('recipes:ingredient_list')
    return render(request, 'recipes/ingredient_confirm_delete.html', {'ingredient': ingredient})


############################### RECIPES

@login_required
def recipe_create(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('recipes:recipe_list')
    else:
        form = RecipeForm()
    return render(request, 'recipes/recipe_form.html', {'form': form})


@login_required
def recipe_list(request: HttpRequest) -> HttpResponse:
    recipes = Recipe.objects.all()
    return render(request, 'recipes/recipe_list.html', {'recipes': recipes})


@login_required
def recipe_update(request: HttpRequest, pk: int) -> HttpResponse:
    recipe = get_object_or_404(Recipe, pk=pk)
    if request.method == 'POST':
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('recipes:recipe_list')
    else:
        form = RecipeForm(instance=recipe)
    return render(request, 'recipes/recipe_form.html', {'form': form})


@login_required
def recipe_delete(request: HttpRequest, pk: int) -> HttpResponse:
    recipe = get_object_or_404(Recipe, pk=pk)
    if request.method == 'POST':
        recipe.delete()
        return redirect('recipes:recipe_list')
    return render(request, 'recipes/recipe_confirm_delete.html', {'recipe': recipe})
