from django.shortcuts import render

# Create your views here.

def blog_home(request):
    return render(request, "app_blog/blog_home.html")