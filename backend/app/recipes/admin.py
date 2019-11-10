from django.contrib import admin
from .models import Ingredients, IngredientsToCompositions, Compositions, RecipesToIngredients, Recipes, RecipesCategory


class IngredientsToCompositionsInline(admin.TabularInline):
    model = IngredientsToCompositions
    extra = 2  # how many rows to show


class IngredientsAdmin(admin.ModelAdmin):
    inlines = (IngredientsToCompositionsInline,)
    model = IngredientsToCompositions
    extra = 2  # how many rows to show


class RecipesToIngredientsInline(admin.TabularInline):
    model = RecipesToIngredients
    extra = 2  # how many rows to show


class RecipesAdmin(admin.ModelAdmin):
    inlines = (RecipesToIngredientsInline,)
    model = Recipes
    extra = 2  # how many rows to show


class CompositionsAdmin(admin.ModelAdmin):
    pass


admin.site.register(Ingredients, IngredientsAdmin)
admin.site.register(Compositions, CompositionsAdmin)
admin.site.register(Recipes, RecipesAdmin)
admin.site.register(RecipesCategory)
