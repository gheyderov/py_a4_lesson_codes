from django.db import models
from core.models import AbstractModel
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
User = get_user_model()

# Create your models here.

class Recipe(AbstractModel):
    category = models.ForeignKey('Category', related_name='recipes', on_delete=models.CASCADE)
    tags = models.ManyToManyField('Tag', related_name='recipes')
    author = models.ForeignKey(User, related_name='recipes', on_delete=models.CASCADE)

    title = models.CharField('title', max_length=155)
    slug = models.SlugField(null=True, blank=True)
    small_description = models.CharField('small_description', max_length=200)
    description = models.TextField('description')
    image = models.ImageField('image', upload_to='recipe_images/')
    cover_image = models.ImageField('cover_image', upload_to='cover_images/')

    def author_name(self):
        return self.author.get_full_name()

    def get_absolute_url(self):
        return reverse_lazy('recipe_detail', kwargs = {'slug' : self.slug})

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
        # ordering = ['-created_at']

    

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
    

class Comment(AbstractModel):
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='children', null=True, blank=True)
    message = models.TextField('messages')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='comments')

    def __str__(self) -> str:
        return f'{self.user.username} / {self.recipe.title}'