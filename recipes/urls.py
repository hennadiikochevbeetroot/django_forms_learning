
from django.urls import path
from . import views

app_name = 'recipes'
urlpatterns = [
    # Main Menu
    path('main_menu/', views.main_menu, name='main_menu'),
    # Categories CRUD
    path('categories/', views.category_list, name='category_list'),
    path('categories/create/', views.category_create, name='category_create'),
    path('categories/<int:pk>/update/', views.category_update, name='category_update'),
    path('categories/<int:pk>/delete/', views.category_delete, name='category_delete'),

    # Ingredients CRUD
    path('ingredients/', views.ingredient_list, name='ingredient_list'),
    path('ingredients/create/', views.ingredient_create, name='ingredient_create'),
    path('ingredients/<int:pk>/update/', views.ingredient_update, name='ingredient_update'),
    path('ingredients/<int:pk>/delete/', views.ingredient_delete, name='ingredient_delete'),

    # Recipes CRUD
]

