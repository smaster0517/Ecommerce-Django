# from django.shortcuts import render
from django.views.generic import ListView, DetailView
from app_store.models import Product

# def home(request):
#     all_products = Product.objects.all()
#     context = {
#         'title' : 'Home', 
#         'all_products' : all_products
#     }
#     return render(request, "app_store/home.html", context)

class FeaturedProductListView(ListView):
    model = Product
    template_name = 'app_store/home.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'all_products'
    ordering = ['-date_posted'] # date_posted - oldest to newest

class ProductDetailView(DetailView):
    model = Product

class StoreProductListView(ListView):
    model = Product
    template_name = 'app_store/store_products.html'
    context_object_name = 'all_products'
    ordering = ['-date_posted']
    paginate_by = 12