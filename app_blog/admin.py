from django.contrib import admin
from .models import Blog, BlogSection

class BlogAdmin(admin.ModelAdmin):
    list_filter = ['read_time', 'date_posted']
    search_fields = ['title']

class BlogSectionAdmin(admin.ModelAdmin):
    list_filter = ['date_posted']
    search_fields = ['blog__title', 'title', 'content']
    list_display = ['blog_title', 'title']
    def blog_title(self, obj):
        return obj.blog.title
    blog_title.short_description = 'Blog Title'

admin.site.register(Blog, BlogAdmin)
admin.site.register(BlogSection, BlogSectionAdmin)