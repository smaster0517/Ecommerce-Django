from itertools import product
from django.shortcuts import render
from app_store.models import Product

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
    all_products = Product.objects.all()
    context = {
        'product' : product,
        'title' : 'Home', 
        'all_products' : all_products
    }
    return render(request, "app_store/home.html", context)