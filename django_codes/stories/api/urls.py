from django.urls import path
from stories.api.views import (
    categories,
    RecipeAPIView,
    RecipeRetrieveUpdateDestroyAPIView,
)
from stories.api.routers import router

urlpatterns = [
    path("categories/", categories, name="categories"),
    # path("recipes/", RecipeAPIView.as_view(), name="recipes"),
    # path("recipe/<int:pk>/", RecipeRetrieveUpdateDestroyAPIView.as_view(), name="recipe_update"),
]

urlpatterns += router.urls