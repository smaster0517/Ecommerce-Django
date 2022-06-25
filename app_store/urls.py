from django.urls import path
from .views import FeaturedProductListView, ProductDetailView, StoreProductListView
from . import views

urlpatterns = [
    # path('', views.home, name='store-home'),
    path('',  FeaturedProductListView.as_view(), name='store-home'),
    path('store/',  StoreProductListView.as_view(), name='store-products'),
    path('product/<int:pk>/',  ProductDetailView.as_view(), name='product-detail')
]