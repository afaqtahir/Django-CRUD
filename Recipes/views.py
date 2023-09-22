from django.shortcuts import render, redirect
from .models import *
# Create your views here.

def recipes(request):
    if request.method == "POST":
        form_data = request.POST
        Recipe.objects.create(
            recipe_name = form_data.get("recipe_name"),
            recipe_description = form_data.get("recipe_description"),
            recipe_image = request.FILES.get("recipe_image")
        )
        return redirect('/recipes')
    return render(request, "recipes.html")
