from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    title = models.CharField(max_length=200)  # Название рецепта
    description = models.TextField()  # Описание
    steps = models.TextField()  # Шаги приготовления
    cooking_time = models.PositiveIntegerField()  # Время приготовления (в минутах)
    image = models.ImageField(upload_to='recipes/', blank=True, null=True)  # Изображение
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # Автор рецепта
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)  # Категории

    def __str__(self):
        return self.title

class RecipeCategory(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

