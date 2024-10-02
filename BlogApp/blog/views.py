from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Blog,Comment
# Create your views here.

def home(request):
    blogs = Blog.objects.all().order_by('-created_at')
    return render(request,'blog/home.html',{"blogs":blogs})

def blog_detail(request, id):
    # Get the blog post by ID or return 404 if not found
    blog = get_object_or_404(Blog, id=id)
    
    # Pass the blog post to the template
    return render(request, 'blog/blog_detail.html', {'blog': blog})
    