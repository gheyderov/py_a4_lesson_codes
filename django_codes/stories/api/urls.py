from django.urls import path
from stories.api.views import (
    categories,
    RecipeAPIView,
    RecipeRetrieveUpdateDestroyAPIView,
    TagListView
)
from stories.api.routers import router

urlpatterns = [
    path("categories/", categories, name="categories"),
    path("tags/", TagListView.as_view(), name="tags"),
    path("recipes/", RecipeAPIView.as_view(), name="recipe-list"),
    path("recipe/<int:pk>/", RecipeRetrieveUpdateDestroyAPIView.as_view(), name="recipe_update"),
]

urlpatterns += router.urls