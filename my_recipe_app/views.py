from django.shortcuts import redirect, render
from my_recipe_app.models import Recipe
from my_recipe_app.forms import RecipeForm

def show_recipe(request, id):
  print('recipe id', id)

  recipe = Recipe.objects.get(id=id)
  print(recipe.title, recipe.description)

  context = {
    'recipe': recipe,
  }
  return render(request, 'my_recipe_app/detail.html', context)


def create_recipe(request):
  if request.method == 'POST':
    form = RecipeForm(request.POST)
    print('form' , form)
    if form.is_valid():
      form.save()
      return redirect('list_recipes')
    else:
      form = RecipeForm()
      context = {
        'form': form,
      }
      return render(request, 'my_recipe_app/create.html', context)
  return render(request, 'my_recipe_app/create.html')

def remove_recipe(request, id):
  print('recipe id', id)

  recipe = Recipe.objects.get(id=id)
  print(recipe.title, recipe.image, recipe.description)

  context = {
    'recipe': recipe,
  }

  if request.method == 'POST':
    input = "hi"
    print("Are you sure you want to delete this recipe?")
    if input.upper == "YES":
      recipe.delete()
      return redirect('list_recipes')
    else:
      input = "ya"
      print("Do you want to go back to the recipe list?")
      if input.upper == "YES":
        return redirect('list_recipes')
    
  return render('list_recipes', context)
  
def modify_recipe(request, id):
  if request.method == "POST":
   form = RecipeForm(request.POST)
   print('form' , form)
   if form.is_valid():
      form.save()
      return redirect('list_recipes')
   else:
      form = RecipeForm()
      context = {
        'form': form,
      }
      return render(request, 'my_recipe_app/modify.html', context)
  return render(request, 'my_recipe_app/modify.html')
  

# def list_recipes(request):
#   return ''