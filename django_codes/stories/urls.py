from django.urls import path
from stories.views import recipes, recipe_detail

urlpatterns = [
    path('recipes/', recipes, name = 'recipes'),
    path('recipe/<int:pk>/', recipe_detail, name = 'recipe_detail'),
]
