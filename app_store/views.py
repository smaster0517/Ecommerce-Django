from django.views.generic import ListView, DetailView
from app_store.models import Product, WishlistProduct
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
        if self.request.user.is_authenticated:
            current_user_wishlist_products = WishlistProduct.objects.all().filter(user=self.request.user)
            current_user_product_id_list = []
            for product in current_user_wishlist_products:
                current_user_product_id_list.append(product.product.id)
            context['current_user_wishlist_products'] = current_user_product_id_list
        return context

class ProductDetailView(DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            current_user_wishlist_products = WishlistProduct.objects.all().filter(user=self.request.user)
            current_user_product_id_list = []
            for product in current_user_wishlist_products:
                current_user_product_id_list.append(product.product.id)
            context['current_user_wishlist_products'] = current_user_product_id_list
        return context

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
    
    def get_context_data(self, **kwargs):
        context = super(StoreProductListView, self).get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            current_user_wishlist_products = WishlistProduct.objects.all().filter(user=self.request.user)
            current_user_product_id_list = []
            for product in current_user_wishlist_products:
                current_user_product_id_list.append(product.product.id)
            context['current_user_wishlist_products'] = current_user_product_id_list
        return context
    
class WishListView(ListView):
    model = WishlistProduct
    template_name = 'app_store/user_wishlist.html'
    context_object_name = 'all_wishlist_products'
    paginate_by = 20

    def get_query_set(self, **kwargs):
        query_set = super(WishListView, self).get_context_data(**kwargs)
        query_set = self.model.objects.all().filter(user=self.request.user).order_by('-date_added')
        return query_set