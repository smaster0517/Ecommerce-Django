from django.contrib import admin
from .models import Product, Image, Wishlist, WishlistProduct

class ProductAdmin(admin.ModelAdmin):
    list_filter = ['featured', 'date_posted']
    search_fields = ['title', 'description']

class ImageAdmin(admin.ModelAdmin):
    search_fields = ['product__title']
    list_display = ['product_title', 'image', 'id']
    def product_title(self, obj):
        return obj.product.title
    product_title.short_description = 'Product Title'

admin.site.register(Product, ProductAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(Wishlist)
admin.site.register(WishlistProduct)