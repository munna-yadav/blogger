from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Blog,Comment
from django.contrib.auth.decorators import login_required
from .forms import BlogForm,CommentForm
from django.views.generic import UpdateView
from django.urls import reverse_lazy
# Create your views here.

def home(request):
    if request.user.is_authenticated:
        blogs = Blog.objects.all().order_by('-created_at')
        return render(request,'blog/home.html',{"blogs":blogs})
    else:
        return redirect('welcome')
    
@login_required
def blog_detail(request, id):
    # Get the blog post by ID or return 404 if not found
    blog = get_object_or_404(Blog, id=id)
    
    # Pass the blog post to the template
    return render(request, 'blog/blog_detail.html', {'blog': blog})

@login_required
def create_blog(request):
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES)
        print(request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.user = request.user
            blog.save()
            return redirect('home')
    else:
        form = BlogForm()
    return render (request,"blog/create_blog.html",{"form":form})


@login_required
def edit_blog(request,blog_id):
    blog = get_object_or_404(Blog,pk=blog_id, user = request.user)
    if request.method == 'POST':
        form =  BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save(commit=False)
            blog.user = request.user
            blog.save()
            return redirect('home')
        pass    
    else:
        form = BlogForm(instance=blog)
    return render(request, 'blog/edit_blog.html',{"form":form})

@login_required
def delete_blog(request,blog_id):
    blog = get_object_or_404(Blog,pk=blog_id, user = request.user)
    if request.method == "POST":
        blog.delete()
        return redirect('home')
    return render(request, 'blog/delete_dialog.html',{"blog":blog})

@login_required
def create_comment(request,blog_id):
    blog = get_object_or_404(Blog,id=blog_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit= False)
            comment.user = request.user
            comment.blog = blog
            comment.save()
            return redirect('blog_detail',blog_id=blog.id)
        
    else:
        form = CommentForm()
    return render(request,'blog/blog_detail.html',{'form':form,'blog':blog,'comment':comment})
    

@login_required
def profile_view(request):
    blogs = Blog.objects.filter(user=request.user).order_by('-created_at')
    return render(request,'blog/profile.html',{'blogs':blogs})