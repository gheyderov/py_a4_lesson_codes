from stories.models import Category, Recipe
from django.http import JsonResponse
from stories.api.serializers import CategorySerializer, RecipeSerializer
from rest_framework.decorators import api_view


def categories(request):
    category_list = Category.objects.all()  # list
    serializer = CategorySerializer(category_list, many = True)
    # category_dict = []
    # for category in category_list:
    #     category_dict.append({"cat_id": category.id, "cat_title": category.title})
    return JsonResponse(data=serializer.data, safe=False)


@api_view(['GET', 'POST'])
def recipes(request):
    if request.method == 'POST':
        serializer = RecipeSerializer(data = request.data, context = {'request':request})
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data = serializer.data, safe = False)
        return JsonResponse(data = serializer.errors, safe = False)
    recipe_list = Recipe.objects.all()
    serializer = RecipeSerializer(recipe_list, context = {'request':request}, many = True)
    return JsonResponse(data = serializer.data, safe = False)