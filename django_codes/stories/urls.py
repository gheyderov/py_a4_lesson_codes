from django.urls import path
from stories.views import recipes, single

urlpatterns = [
    path('recipes/', recipes, name = 'recipes'),
    path('single/', single, name = 'single'),
]
