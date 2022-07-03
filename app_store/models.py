from django.db import models
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
        return self.title

class Images(models.Model):
    image = models.ImageField(default='default.jpg', upload_to='product_pics')
    product = models.ForeignKey(Product, null=True, on_delete=models.CASCADE)