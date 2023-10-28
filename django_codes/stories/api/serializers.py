from rest_framework import serializers
from stories.models import Category, Recipe, Tag


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "title")


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ("id", "title")



class RecipeCreateSerializer(serializers.ModelSerializer):

    slug = serializers.SlugField(read_only = True)

    class Meta:
        model = Recipe
        fields = (
            'id',
            'title',
            'category',
            'tags',
            'slug',
            'small_description',
            'description',
            'image',
            'cover_image',
            'author'
        )


class RecipeSerializer(serializers.ModelSerializer):

    category = CategorySerializer()
    tags = TagSerializer(many = True)

    class Meta:
        model = Recipe
        fields = (
            'id',
            'title',
            'category',
            'tags',
            'slug',
            'small_description',
            'description',
            'image',
            'cover_image',
            'author_name'
        )
