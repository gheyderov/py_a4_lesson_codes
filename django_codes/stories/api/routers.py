from rest_framework.routers import DefaultRouter
from stories.api.views import RecipeViewSet

router = DefaultRouter()
router.register(r'recipes', RecipeViewSet)