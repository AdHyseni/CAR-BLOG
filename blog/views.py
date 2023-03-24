from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import *
from .forms import CommentForm
from django.views.generic import ListView,DetailView,View



# Create your views here.
def home(request):
    return render(request, 'blog/home.html')

def about(request):
    return render(request, 'blog/about.html')

def blogs(request):
    blogs = Blog.objects.all()
    return render(request, 'blog/blogs.html',{'blogs':blogs})

class BlogDetails(View):

    def get(self, request, slug):
        blog = Blog.objects.get(slug=slug)
        context = {
            'blog':blog,
            'comment_form':CommentForm(),
            'comments': blog.comments.all().order_by('-id'),
            'kategori':blog.kategori.all(),
        }
        return render(request,'blog/blog.html',context)
    def post(self, request,slug):
        comment_form = CommentForm(request.POST)
        post = Blog.objects.get(slug=slug)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse("blog", args=[slug]))
        
        
        context = {
            'post':post,
            'comment_form':CommentForm(),
            'comments': post.comments.all().order_by('-id'),
            'kategori':post.kategori.all(),
        }
        return render(request,'blog/blog.html',context)

def contact(request):
    return render(request, 'blog/contact.html')
