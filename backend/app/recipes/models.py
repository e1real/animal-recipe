from django.db import models


class NameModel(models.Model):
    name = models.CharField(verbose_name='Наименование', max_length=255)

    def __str__(self):
        return self.name

    class Meta(object):
        abstract = True


class Compositions(NameModel):
    """Состав ингредиентов"""

    class Meta:
        verbose_name = 'Состав ингредиента'
        verbose_name_plural = 'Состав ингредиентов'


class Ingredients(NameModel):
    """Ингредиенты"""
    compositions = models.ManyToManyField(Compositions, through='IngredientsToCompositions')

    class Meta:
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'


class IngredientsToCompositions(models.Model):
    """Связь между ингредиентом и его составом"""
    composition = models.ForeignKey(Compositions, on_delete=models.DO_NOTHING, verbose_name='Состав')
    ingredients = models.ForeignKey(Ingredients, on_delete=models.DO_NOTHING, verbose_name='Ингредиенты')
    percentage = models.DecimalField(verbose_name='процент ввода', blank=True, null=True, max_digits=5,
                                     decimal_places=2, help_text='процент ввода ингредиента')

    def __str__(self):
        return self.composition.name

    class Meta:
        verbose_name = 'Состав ингредиентов'
        verbose_name_plural = 'Состав ингредиентов'


class RecipesCategory(NameModel):
    """Категория рецептов"""

    class Meta:
        verbose_name = 'Категория рецепта'
        verbose_name_plural = 'Категория рецепта'


class Recipes(NameModel):
    """Рецепты"""
    ingredients = models.ManyToManyField(Ingredients, through='RecipesToIngredients')
    category = models.ForeignKey(RecipesCategory, on_delete=models.DO_NOTHING, null=True, blank=True,
                                 verbose_name='Категория рецепта')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'


class RecipesToIngredients(models.Model):
    """Связь между рецептом и ингредиентом"""
    recipes = models.ForeignKey(Recipes, on_delete=models.DO_NOTHING)
    ingredients = models.ForeignKey(Ingredients, on_delete=models.DO_NOTHING)
    percentage = models.DecimalField(verbose_name='процент ввода', blank=True, null=True, max_digits=4,
                                     decimal_places=2, help_text='процент ввода ингредиента')

    class Meta:
        verbose_name = 'Ингредиент рецепта'
        verbose_name_plural = 'Ингредиенты рецепта'
