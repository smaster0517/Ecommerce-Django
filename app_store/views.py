from django.views.generic import ListView, DetailView
from app_store.models import Product
from functools import reduce
import operator
from django.db.models import Q

class FeaturedProductListView(ListView):
    model = Product
    template_name = 'app_store/home.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'all_products'
    ordering = ['-date_posted']

class ProductDetailView(DetailView):
    model = Product

class StoreProductListView(ListView):
    model = Product
    template_name = 'app_store/store_products.html'
    context_object_name = 'all_products'
    paginate_by = 12

    def get_queryset(self):
        query = self.request.GET.get('search')
        if query:
            query = query.split()
            object_list = self.model.objects.filter(reduce(operator.or_, (Q(title__icontains = search_word) for search_word in query)))
            return object_list
        return Product.objects.all().order_by('-date_posted')