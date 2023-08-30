from django.shortcuts import render
from stories.models import Recipe

# Create your views here.

def recipes(request):
    recipe = Recipe.objects.all()
    context = {
        'recipe_list' : recipe
    }
    return render(request, 'recipes.html', context)

def stories(request):
    return render(request, 'stories.html')

def single(request):
    return render(request, 'single.html')