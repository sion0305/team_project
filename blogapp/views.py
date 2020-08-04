from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Blog
from .forms import NewBlog

def welcome(request):
    return render(request, 'welcome.html')

def home(request):
    blogs = Blog.objects.all()
    paginator = Paginator(blogs, 3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'home.html',{'blogs':blogs, 'posts':posts})

def create(request):
    if request.method == "POST":
        form = NewBlog(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit = False)
            post.pub_date = timezone.now()
            post.save()
            return redirect('home')
    else:
        form = NewBlog()
        return render(request,'new.html', {'form':form})
   
def update(request, pk):
    blog = get_object_or_404(Blog, pk = pk)
    if request.method == 'POST':
        form = NewBlog(request.POST, request.FILES, instance = blog)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = NewBlog(instance= blog)
        return render(request, 'new.html', {'form':form})

def delete(request, pk):
    blog = get_object_or_404(Blog, pk = pk)
    blog.delete()
    return redirect('home')

def detail(request, pk):
    blog = get_object_or_404(Blog, pk = pk)
    
    return render(request, 'detail.html', {'blog':blog})
