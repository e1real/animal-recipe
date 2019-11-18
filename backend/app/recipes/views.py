from .models import Recipes, Ingredients, Compositions, IngredientsToCompositions
from .serializers import RecipesSerializer, IngredientsSerializer, CompositionsSerializer, \
    IngredientsToCompositionsSerializer, DefaultRecipesSerializer
from rest_framework import viewsets


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
