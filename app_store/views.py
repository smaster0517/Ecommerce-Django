from django.views.generic import ListView, DetailView
from app_store.models import Product
from functools import reduce
import operator
from django.db.models import Q
from django.shortcuts import render

def about(request):
    return render(request, "app_store/about.html")

class FeaturedProductListView(ListView):
    model = Product
    template_name = 'app_store/home.html' # <app>/<model>_<viewtype>.html

    def get_context_data(self, **kwargs):
        context = super(FeaturedProductListView, self).get_context_data(**kwargs)
        context['all_featured_products'] = self.model.objects.filter(featured=True).all().order_by('-date_posted')
        return context

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