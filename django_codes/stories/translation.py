from modeltranslation.translator import translator, TranslationOptions
from stories.models import Category, Recipe

class RecipeTranslationOptions(TranslationOptions):
    fields = ('title',)

translator.register(Category, RecipeTranslationOptions)


class CategoryTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

translator.register(Recipe, CategoryTranslationOptions)