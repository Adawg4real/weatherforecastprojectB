from django.forms import ModelForm
from my_recipe_app.models import Recipe

class RecipeForm(ModelForm):
  class Meta:
    model = Recipe
    fields -(
      'title',
      'picture',
      'descriptio'
    )