from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from django_select2.forms import Select2MultipleWidget, Select2Widget

from .models import Category, Ingredient, Recipe


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.add_input(Submit('submit', 'Save Category'))


class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ['name', 'type', 'cost_per_kg']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.add_input(Submit('submit', 'Save Ingredient'))


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 'content', 'category', 'ingredients']
        widgets = {
            'category': Select2Widget,
            'ingredients': Select2MultipleWidget,
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.add_input(Submit('submit', 'Save Recipe'))

        # Many to One, form basic select
        self.fields['category'].queryset = Category.objects.all()
        self.fields['category'].widget.attrs.update({'class': 'form-control'})
        # Many to Many, form multi-select
        self.fields['ingredients'].queryset = Ingredient.objects.all()
        self.fields['ingredients'].widget.attrs.update({'class': 'form-control select2'})
