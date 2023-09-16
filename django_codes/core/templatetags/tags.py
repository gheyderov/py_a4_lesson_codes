from django.template import Library
register = Library()
from stories.models import Category, Recipe


@register.simple_tag
def get_categories(limit = 5):
    return Category.objects.all()[:limit]


# @register.filter
# def uppers(value):
#     return value.upper()


@register.inclusion_tag('includes/related_products.html')
def related_products():
    recipes = Recipe.objects.order_by('created_at')
    context = {
        'related_recipes' : recipes
    }
    return context