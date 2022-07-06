from django.db import models
from django.utils import timezone

class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    read_time = models.IntegerField(default=0)
    image = models.ImageField(default='default.jpg', upload_to='blog_pics')
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class BlogSection(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(default='default.jpg', upload_to='product_pics')
    date_posted = models.DateTimeField(default=timezone.now)
    blog = models.ForeignKey(Blog, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title