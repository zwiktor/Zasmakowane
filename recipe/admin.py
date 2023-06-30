from django.contrib import admin
from recipe.models import Recipe, Ingredient, Category, Cuisine, Tag, Step, Ingedient_group, Post

# Register your models here.

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    exclude = ('slug',)

# @admin.register(Step)
# class RecipeAdmin(admin.ModelAdmin):
#     exclude = ('number',)

admin.site.register(Step)
admin.site.register(Ingedient_group)
admin.site.register(Ingredient)
admin.site.register(Category)
admin.site.register(Cuisine)
admin.site.register(Tag)
admin.site.register(Post)
