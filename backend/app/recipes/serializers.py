from rest_framework import serializers
from .models import Compositions, Recipes, Ingredients, IngredientsToCompositions


class IngredientsToCompositionsSerializer(serializers.ModelSerializer):
    # id = serializers.ReadOnlyField(source='ingredient.id')
    # name = serializers.ReadOnlyField(source='ingredient.name')
    # percentage = serializers.DecimalField(decimal_places=2, max_digits=5)
    composition_name = serializers.ReadOnlyField(source='composition.name')
    composition_id = serializers.ReadOnlyField(source='composition.id')

    class Meta:
        model = IngredientsToCompositions
        fields = ('id', 'percentage', 'composition_name', 'composition_id')


class CompositionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compositions
        fields = '__all__'


class IngredientsSerializer(serializers.ModelSerializer):
    compositions = serializers.SerializerMethodField()

    class Meta:
        model = Ingredients
        fields = ('id', 'name', 'compositions')

    def get_compositions(self, obj):
        queryset = obj.ingredientstocompositions_set.all()
        serializer = IngredientsToCompositionsSerializer(queryset, many=True)
        return serializer.data


class RecipesSerializer(serializers.ModelSerializer):
    ingredients = IngredientsSerializer(many=True, read_only=True)

    class Meta:
        model = Recipes
        fields = '__all__'
