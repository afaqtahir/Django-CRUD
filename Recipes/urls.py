from django.urls import path
from . import views


urlpatterns = [
    path('', views.recipes),
    path('DeleteRecipe/<int:id>/', views.delete_recipe),
    path('UpdateRecipe/<int:id>/', views.update_recipe)
]