from rest_framework import serializers
from .models import Compositions, Recipes, Ingredients, IngredientsToCompositions
from rest_framework.utils import model_meta


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


class DefaultIngredientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredients
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
    ingredients = DefaultIngredientsSerializer(many=True)

    def create(self, validated_data):
        ingredients = validated_data.pop('ingredients')
        recipe = Recipes.objects.create(**validated_data)
        # for ingredient in ingredients:
        #     Ingredients.objects.create(album=recipe, **ingredient)
        return recipe

    def update(self, instance, validated_data):
        # info = model_meta.get_field_info(instance)
        # m2m_fields = []
        # for attr, value in validated_data.items():
        #     if attr in info.relations and info.relations[attr].to_many:
        #         m2m_fields.append((attr, value))
        #     else:
        #         setattr(instance, attr, value)
        #
        # instance.save()
        #
        # # Note that many-to-many fields are set after updating instance.
        # # Setting m2m fields triggers signals which could potentially change
        # # updated instance and we do not want it to collide with .update()
        # for attr, value in m2m_fields:
        #     field = getattr(instance, attr)
        #     field.set(value)
        email = self.validated_data.get()
        message = self.validated_data['message']
        instance.save()
        return instance

    class Meta:
        model = Recipes
        fields = '__all__'


class DefaultRecipesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipes
        fields = '__all__'
