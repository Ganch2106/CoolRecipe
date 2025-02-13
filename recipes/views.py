from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import Recipe, Category
from .forms import RecipeForm
from .forms import CustomUserCreationForm

# Главная страница
def home(request):
    categories = Category.objects.all()
    recipes = Recipe.objects.order_by('?')[:5]  # 5 случайных рецептов
    return render(request, 'recipes/home.html', {'categories': categories, 'recipes': recipes})

# Детальная страница рецепта
def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe})

# Фильтр рецептов по категории
def recipes_by_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    recipes = Recipe.objects.filter(category=category)
    return render(request, 'recipes/category_recipes.html', {'category': category, 'recipes': recipes})

# Добавление/редактирование рецепта
@login_required(login_url='login')
def add_edit_recipe(request, recipe_id=None):
    if recipe_id:
        recipe = get_object_or_404(Recipe, id=recipe_id)
    else:
        recipe = None

    if request.method == "POST":
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            new_recipe = form.save(commit=False)
            new_recipe.author = request.user
            new_recipe.save()
            return redirect('home')
    else:
        form = RecipeForm(instance=recipe)

    return render(request, 'recipes/add_edit_recipe.html', {'form': form, 'recipe': recipe})


# Удаление рецепта с подтверждением
@login_required
def delete_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id, author=request.user)

    if request.method == "POST":
        recipe.delete()
        return redirect('home')  # Перенаправление на главную

    return render(request, 'recipes/delete_recipe.html', {'recipe': recipe})

# Вход пользователя
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'recipes/login.html', {'form': form})

# Выход пользователя
def logout_view(request):
    logout(request)
    return redirect('home')

# Регистрация пользователя
def register_view(request):
    if request.method == "POST":
        print(request.POST)
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Перенаправляем пользователя на страницу входа
    else:
        form = UserCreationForm()

    return render(request, 'recipes/register.html', {'form': form})
