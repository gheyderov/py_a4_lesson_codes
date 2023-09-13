from django.contrib import admin
from django import forms
from stories.models import Recipe, Category, Tag, Property, PropertyValue, RecipeImage

# Register your models here.



admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Property)
admin.site.register(PropertyValue)
admin.site.register(RecipeImage)


class RecipeAdminForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'
        widgets = {
            'tags' : forms.CheckboxSelectMultiple
        }


class RecipeInline(admin.TabularInline):
    model = RecipeImage


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category', 'author', 'get_tags']
    list_display_links = ['id', 'title']
    list_editable = ['category']
    # list_per_page = 2
    list_max_show_all = 1
    search_fields = ['title', 'category__title']
    list_filter = ['category', 'tags']
    inlines = [RecipeInline]
    form = RecipeAdminForm

    def get_tags(self, obj):
        arr = []
        for tag in obj.tags.all():
            arr.append(tag)
        return arr
    
    # fieldsets = [
    #     (
    #         "Main fields",
    #         {
    #             "fields": ["title", "category", "tags"],
    #         },
    #     ),
    #     (
    #         "Other options",
    #         {
    #             "classes": ["collapse"],
    #             "fields": ["small_description", "description", 'image'],
    #         },
    #     ),
    # ]