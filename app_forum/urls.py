from django.urls import path
from . import views

urlpatterns = [
    path('', views.forum_home, name='forum-home')
]