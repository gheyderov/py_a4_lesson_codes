from stories.models import Category, Recipe
from django.http import JsonResponse
from stories.api.serializers import CategorySerializer, RecipeSerializer, RecipeCreateSerializer
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializers = {
        'default' : RecipeSerializer,
        'create' : RecipeCreateSerializer,
        'update' : RecipeCreateSerializer
    }

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.serializers['default'])


class RecipeRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeCreateSerializer
    


class RecipeAPIView(ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return RecipeCreateSerializer
        return self.serializer_class


def categories(request):
    category_list = Category.objects.all()  # list
    serializer = CategorySerializer(category_list, many = True)
    # category_dict = []
    # for category in category_list:
    #     category_dict.append({"cat_id": category.id, "cat_title": category.title})
    return JsonResponse(data=serializer.data, safe=False)


# @api_view(['GET', 'POST'])
# def recipes(request):
#     if request.method == 'POST':
#         serializer = RecipeCreateSerializer(data = request.data, context = {'request':request})
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(data = serializer.data, safe = False, status = 201)
#         return JsonResponse(data = serializer.errors, safe = False, status = 400)
#     recipe_list = Recipe.objects.all()
#     serializer = RecipeSerializer(recipe_list, context = {'request':request}, many = True)
#     return JsonResponse(data = serializer.data, safe = False)


# @api_view(['PUT', 'PATCH'])
# def recipe_update(request, pk):
#     if request.method == 'PUT':
#         recipe = Recipe.objects.get(id = pk)
#         serializer = RecipeCreateSerializer(data = request.data, instance = recipe, context = {'request':request})
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(data = serializer.data, safe = False, status = 201)
#         return JsonResponse(data = serializer.errors, safe = False, status = 400)
#     if request.method == 'PATCH':
#         recipe = Recipe.objects.get(id = pk)
#         serializer = RecipeCreateSerializer(data = request.data, partial = True, instance = recipe, context = {'request':request})
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(data = serializer.data, safe = False, status = 201)
#         return JsonResponse(data = serializer.errors, safe = False, status = 400)
#     recipe_list = Recipe.objects.all()
#     serializer = RecipeSerializer(recipe_list, context = {'request':request}, many = True)
#     return JsonResponse(data = serializer.data, safe = False)