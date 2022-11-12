from django.views.generic import ListView, DetailView
from app_store.models import Product, WishlistProduct, Wishlist
from functools import reduce
import operator, json
from django.db.models import Q
from django.shortcuts import render
from django.http import JsonResponse

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
    paginate_by = 24

    def get_queryset(self, **kwargs):
        query_set = self.model.objects.all().filter(user=self.request.user).order_by('-date_added')
        return query_set

def api_update_wishlist(request):
    json_data = json.loads(request.body)
    product_id = json_data['productID']

    if WishlistProduct.objects.filter(product__id=product_id, user=request.user).exists():
        # removes entry from wishlist
        WishlistProduct.objects.filter(product__id=product_id, user=request.user).delete()
        return JsonResponse({'data':'Add to Wishlist'})
    else:
        # adds entry to wishlist
        product = Product.objects.get(id=product_id)
        wishlist = Wishlist.objects.get(user=request.user)
        new_wishlist_product = WishlistProduct(user=request.user, Wishlist=wishlist, product=product)
        new_wishlist_product.save()
        return JsonResponse({'data':'Remove from Wishlist'})