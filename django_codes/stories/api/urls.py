from django.urls import path
from stories.api.views import categories, recipes

urlpatterns = [
    path('categories/', categories, name = 'categories'),
    path('recipes/', recipes, name = 'recipes')
]