from django.urls import path
from stories.views import (
    RecipeListView,
    RecipeDetailView,
    like_post,
    RecipeCreateView,
    RecipeUpdateView,
)

urlpatterns = [
    path("recipes/", RecipeListView.as_view(), name="recipes"),
    path("recipe-create/", RecipeCreateView.as_view(), name="recipe_create"),
    path("recipe-update/<int:pk>/", RecipeUpdateView.as_view(), name="recipe_update"),
    path("like_post/<int:pk>/", like_post, name="like_post"),
    path("recipe/<slug:slug>/", RecipeDetailView.as_view(), name="recipe_detail"),
]
