from django.urls import path

from .views import RecipesViewSet
app_name = "recipes"

urlpatterns = [
    # ex: /polls/
    # path('', views.index, name='index'),
    # path('recipes/create', views.create, name='recipes-create'),
    path('recipes/', RecipesViewSet.as_view())
]
