from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(verbose_name='Category Name', max_length=100)
    description = models.TextField(verbose_name='Category Description')

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(verbose_name='Ingredient Name', max_length=100)
    type = models.CharField(verbose_name='Ingredient Type', max_length=50)
    cost_per_kg = models.FloatField(verbose_name='Ingredient Cost Per KG')

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField(verbose_name='Recipe Name', max_length=100)
    content = models.TextField(verbose_name='Recipe Content')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    ingredients = models.ManyToManyField(Ingredient)

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name
