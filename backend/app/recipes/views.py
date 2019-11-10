from django.shortcuts import render
from .models import Recipes, Ingredients, Compositions, IngredientsToCompositions
from .serializers import RecipesSerializer, IngredientsSerializer, CompositionsSerializer, IngredientsToCompositionsSerializer
from rest_framework import viewsets


def index(request):
    context = {
        'recipes': Recipes.objects.all()
    }
    return render(request, 'index.html', context)


def create(request):
    ingredients = Ingredients.objects.all()
    compositions = Compositions.objects.all()
    context = {
        'ingredients': ingredients,
        'compositions': compositions
    }
    return render(request, 'recipes/create.html', context)


class RecipesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Recipes.objects.all()
    serializer_class = RecipesSerializer


class IngredientsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Ingredients.objects.all()
    serializer_class = IngredientsSerializer


class CompositionsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Compositions.objects.all()
    serializer_class = CompositionsSerializer


class IngredientsToCompositionsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = IngredientsToCompositions.objects.all()
    serializer_class = IngredientsToCompositionsSerializer
