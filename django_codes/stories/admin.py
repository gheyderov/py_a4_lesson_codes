from django.contrib import admin
from django import forms
from stories.models import (
    Recipe,
    Category,
    Tag,
    Property,
    PropertyValue,
    RecipeImage,
    Comment,
    Subscriber
)
from modeltranslation.admin import TranslationAdmin

# Register your models here.


@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    list_display = ["title"]


admin.site.register(Tag)
admin.site.register(Property)
admin.site.register(PropertyValue)
admin.site.register(RecipeImage)
admin.site.register(Comment)
admin.site.register(Subscriber)


class RecipeAdminForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = "__all__"
        widgets = {"tags": forms.CheckboxSelectMultiple}


class RecipeInline(admin.TabularInline):
    model = RecipeImage


@admin.register(Recipe)
class RecipeAdmin(TranslationAdmin):
    list_display = ["id", "title", "category", "author", "get_tags"]
    list_display_links = ["id", "title"]
    list_editable = ["category"]
    # list_per_page = 2
    list_max_show_all = 1
    search_fields = ["title", "category__title"]
    list_filter = ["category", "tags"]
    inlines = [RecipeInline]
    form = RecipeAdminForm
    readonly_fields = ["slug"]

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
