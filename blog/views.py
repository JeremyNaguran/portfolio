from django.shortcuts import render, get_object_or_404
from .models import Blog

# Create your views here.

def blogs(request):
    blogs = Blog.objects
    context = {"blogs": blogs}
    return render(request, 'blog/blogs.html', context)

def details(request, blog_id):
    blog_detial = get_object_or_404(Blog, pk=blog_id)
    context = {"blog_detail": blog_detial}
    return render(request, 'blog/detail.html', context)


