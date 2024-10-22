
from django.urls import path

from . import views

app_name = 'recipes'
urlpatterns = [
    # Main menu
    path('main_menu/', view=views.main_menu, name='main_menu'),
    # Category CRUD
    # path('category/create/', view=views.category_create, name='category_create'),
    path('category/list/', view=views.category_list, name='category_list'),
    # path('category/<int:pk>/edit/', view=views.category_edit, name='category_edit'),
    # path('category/<int:pk>/delete/', view=views.category_delete, name='category_delete'),

    # Ingredient CRUD
    # Recipe CRUD
]

