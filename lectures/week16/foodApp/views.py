from django.shortcuts import render, redirect
from .models import *

meals = [
    'Lunch',
    'Dinner'
]

def index(request):
    allFood = Food.objects.all().values()
    context = {
        'foods': allFood,
        'meals': meals
    }
    return render(request,'index.html', context)

def createFood(request):
    Food.objects.create(
        name='Chicken Nuggets',
        meal='Dinner',
        servings=3
    )
    return redirect('/')