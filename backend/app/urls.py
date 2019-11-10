"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from app.recipes.views import RecipesViewSet, IngredientsViewSet, CompositionsViewSet, IngredientsToCompositionsViewSet

admin.site.site_header = "Администрирование приложения комбикорм для лошадей"
admin.site.site_title = "Комбикорм для лошадей"
admin.site.index_title = "Добро пожаловать"


router = routers.DefaultRouter()
router.register(r'api/recipes', RecipesViewSet)
router.register(r'api/ingredients', IngredientsViewSet)
router.register(r'api/compositions', CompositionsViewSet)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('djoser.urls')),
    path('api/auth/', include('djoser.urls.authtoken')),
    # path('api/recipes/', include('app.recipes.urls')),
]
urlpatterns += router.urls
