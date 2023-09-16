from django.shortcuts import render, get_object_or_404
from stories.models import Recipe, Category, Tag

# Create your views here.

def recipes(request):
    recipe = Recipe.objects.all()
    context = {
        'recipe_list' : recipe
    }
    return render(request, 'recipes.html', context)

def stories(request):
    return render(request, 'stories.html')

def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, id = pk)
    categories = Category.objects.all()
    tags = Tag.objects.all()
    context = {
        'recipe' : recipe,
        'categories' : categories,
        'tags' : tags
    }
    return render(request, 'single.html', context)