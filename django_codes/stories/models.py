from django.db import models
from core.models import AbstractModel
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.

class Recipe(AbstractModel):
    category = models.ForeignKey('Category', related_name='recipes', on_delete=models.CASCADE)
    tags = models.ManyToManyField('Tag', related_name='recipes')
    author = models.ForeignKey(User, related_name='recipes', on_delete=models.CASCADE)
    property_values = models.ManyToManyField('PropertyValue', related_name='recipes', blank=True)
    slug = models.SlugField('Slug', max_length=200)

    title = models.CharField('title', max_length=155)
    small_description = models.CharField('small_description', max_length=200)
    description = models.TextField('description')
    image = models.ImageField('image', upload_to='recipe_images/')
    cover_image = models.ImageField('cover_image', upload_to='cover_images/')

    def __str__(self):
        return self.title
    

class RecipeImage(AbstractModel):
    recipe = models.ForeignKey('Recipe', related_name='images', on_delete=models.CASCADE)
    image = models.ImageField('image', upload_to='recipe_images/')

    def __str__(self):
        return self.recipe.title


class Category(AbstractModel):
    parent = models.ForeignKey('self', related_name='children', on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField('title', max_length=155)


    def __str__(self):
        if self.parent:
            return f'{self.parent} / {self.title}'
        return self.title

    class Meta:
        verbose_name_plural = 'Categories'
        # ordering = ['created_at']

    

class Tag(AbstractModel):
    title = models.CharField('title', max_length=155)

    def __str__(self):
        return self.title
    

class Property(AbstractModel):
    title = models.CharField('title', max_length=155)

    def __str__(self):
        return self.title
    

class PropertyValue(AbstractModel):
    property = models.ForeignKey('Property', related_name='property_values', on_delete=models.CASCADE)
    title = models.CharField('title', max_length=155)

    def __str__(self):
        return self.title