from django.urls import path
from . import views

urlpatterns = [
    # Главная страница
    path('', views.home, name='home'),

    # Детальная страница рецепта
    path('recipe/<int:recipe_id>/', views.recipe_detail, name='recipe_detail'),

    # Фильтр рецептов по категории
    path('category/<int:category_id>/', views.recipes_by_category, name='recipes_by_category'),

    # Добавление и редактирование рецепта
    path('recipe/add/', views.add_edit_recipe, name='add_recipe'),
    path('recipe/<int:recipe_id>/edit/', views.add_edit_recipe, name='edit_recipe'),

    # Удаление рецепта с подтверждением
    path('recipe/<int:recipe_id>/delete/', views.delete_recipe, name='delete_recipe'),

    # Вход, выход и регистрация
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
]
