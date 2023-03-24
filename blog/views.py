from django.shortcuts import render,get_object_or_404
from .models import *


# Create your views here.
def home(request):
    return render(request, 'blog/home.html')

def about(request):
    return render(request, 'blog/about.html')

def blogs(request):
    blogs = Blog.objects.all()
    return render(request, 'blog/blogs.html',{'blogs':blogs})

def blog(request,slug):
    blog = get_object_or_404(Blog, slug=slug)
    return render(request, 'blog/blog.html', {'blog':blog})

def contact(request):
    return render(request, 'blog/contact.html')
