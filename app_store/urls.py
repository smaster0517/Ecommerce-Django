from django.urls import path
from .views import FeaturedProductListView, ProductDetailView, StoreProductListView, WishListView
from . import views

urlpatterns = [
    path('about/', views.about, name='store-about'),
    path('', FeaturedProductListView.as_view(), name='store-home'),
    path('store/', StoreProductListView.as_view(), name='store-products'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('wishlist/', WishListView.as_view(), name='wishlist-products'),
    path('api_update_wishlist/', views.api_update_wishlist, name='update-wishlist'),
    path('api_delete_product/', views.api_delete_product, name='delete-product')
]