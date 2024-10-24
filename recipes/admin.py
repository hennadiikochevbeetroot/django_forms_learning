from django.contrib import admin

from .models import Category, Ingredient, Recipe


class CategoryAdmin(admin.ModelAdmin):
    fieldsets = [
        ('General', {'fields': ['name', 'description']}),
        ('User Reference', {'fields': ['user']}),
    ]


# class IngredientInline(admin.StackedInline):
#     model = Ingredient
#     extra = 3


class RecipeAdmin(admin.ModelAdmin):
    fieldsets = [
        ('General', {'fields': ['name', 'content']}),
        ('Foreign Keys', {'fields': ['category', 'ingredients']}),
    ]


# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Ingredient)
admin.site.register(Recipe, RecipeAdmin)
