from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # phone_number = models.CharField() #TODO pip install django-phone-field
    profile_image = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return f'{self.user} profile'