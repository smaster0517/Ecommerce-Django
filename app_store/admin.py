from django.contrib import admin
from .models import Product, Image, Wishlist, WishlistProduct

admin.site.register(Product)
admin.site.register(Image)
admin.site.register(Wishlist)
admin.site.register(WishlistProduct)