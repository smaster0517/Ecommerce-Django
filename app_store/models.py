from django.db import models
from django.utils import timezone

class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    sold_items = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)
    #TODO images
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title