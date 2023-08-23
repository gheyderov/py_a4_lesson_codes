from django.shortcuts import render

# Create your views here.

def recipes(request):
    return render(request, 'recipes.html')

def stories(request):
    return render(request, 'stories.html')