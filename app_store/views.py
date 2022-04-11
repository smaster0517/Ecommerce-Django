from itertools import product
from django.shortcuts import render

# Create your views here.

# Pseudocode for context variables
product = [
    {
        'title' : 'Sony PS5',
        'description' : 'Electronic Item For Sale',
        'date_posted' : 'January 1, 2022'
    }, 
    {
        'title' : 'Satiety Zombie',
        'description' : 'Art Item For Sale',
        'date_posted' : 'January 10, 2022'
    }
]

def home(request):
    context = {
        'product' : product,
        'title' : 'Home'
    }
    return render(request, "app_store/home.html", context)