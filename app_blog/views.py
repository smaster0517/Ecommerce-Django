from django.views.generic import ListView, DetailView
from .models import Blog

# def blog_home(request):
#     return render(request, "app_blog/blog_home.html")

class BlogListView(ListView):
    model = Blog
    template_name = 'app_blog/blog_home.html'
    context_object_name = 'all_blogs'
    ordering = ['-date_posted']
    paginate_by = 12

class BlogDetailView(DetailView):
    model = Blog