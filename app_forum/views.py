from django.shortcuts import render

# Create your views here.

def forum_home(request):
    return render(request, "app_forum/forum_home.html")