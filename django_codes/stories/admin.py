from django.contrib import admin
from stories.models import Recipe, Category, Tag, Property, PropertyValue

# Register your models here.


admin.site.register(Recipe)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Property)
admin.site.register(PropertyValue)