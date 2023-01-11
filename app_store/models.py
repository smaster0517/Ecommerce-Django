from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    featured = models.BooleanField(default=False)
    available_items = models.IntegerField(default=0)
    thumbnail_image = models.ImageField(default='default.jpg', upload_to='product_pics')
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.title} (${self.price})'

class Image(models.Model):
    image = models.ImageField(default='default.jpg', upload_to='product_pics')
    product = models.ForeignKey(Product, null=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'Image for {self.product.title} (${self.product.price})'

class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(default='Wishlist', max_length=20)

    def __str__(self):
        return f'Wishlist Name: {self.user.username} {self.name}'

'''
many-to-one (User and WLP) - a User can be associated with many WishlistProduct objects,
    but a  WishlistProduct can only have one User object.
many-to-one (Product and WLP) - a Product can be associated with many WishlistProduct objects,
    but a  WishlistProduct can only have one Product object.
many-to-one (WL and WLP) - Wishlist can be associated with many WishlistProduct objects,
    but a WishlistProduct can only have one Wishlist object:
'''
class WishlistProduct(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    wishlist = models.ForeignKey(Wishlist, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date_added = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f'Wishlist Product:{self.product.title} for:{self.user.username}'