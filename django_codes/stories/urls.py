from django.urls import path
from stories.views import recipes

urlpatterns = [
    path('recipes/', recipes, name = 'recipes')
]
