from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
# Create your views here.

def recipes(request):

    if request.method == "GET":
        context = {'recipes': Recipe.objects.all()}
        return render(request, "recipes.html", context)

    elif request.method == "POST":
        form_data = request.POST
        Recipe.objects.create(
            recipe_name = form_data.get("recipe_name"),
            recipe_description = form_data.get("recipe_description"),
            recipe_image = request.FILES.get("recipe_image")
        )
        return redirect('/recipes')

def delete_recipe(request, id):
    recipe = Recipe.objects.get(id=id)
    res = recipe.delete()
    print(res)
    return redirect('/recipes')

def update_recipe(request, id):
    recipe = Recipe.objects.get(id=id)
    context = {'recipe': recipe}
    if request.method == 'POST':
        recipe.recipe_name = request.POST.get('recipe_name')
        recipe.recipe_description = request.POST.get('recipe_description')
        image = request.FILES.get('recipe_image')
        if image:
            recipe.recipe_image = image
        recipe.save()
        return redirect('/recipes')
    return render(request, "update_recipe.html", context)
