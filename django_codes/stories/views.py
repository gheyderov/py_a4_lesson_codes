from django.shortcuts import render, get_object_or_404, HttpResponse
from stories.models import Recipe, Category, Tag
from django.contrib import messages

# Create your views here.

def recipes(request):
    print('Liked Posts: ', request.session.get('liked_posts'))
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

# def like_post(request, pk):
#     request.session['liked_posts'] = request.session.get('liked_posts', ' ') + str(pk) + ' '
#     messages.add_message(request, messages.SUCCESS, "Liked!")
#     return render(request, 'recipes.html')

def like_post(request, pk):
    response = HttpResponse('test')
    response.set_cookie('liked_posts', request.COOKIES.get('liked_posts', ' ') + str(pk) + ' ')
    return response