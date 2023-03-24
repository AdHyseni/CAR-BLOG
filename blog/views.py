from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'blog/home.html')

def about(request):
    return render(request, 'blog/about.html')

def blogs(request):
    return render(request, 'blog/blogs.html')

def contact(request):
    return render(request, 'blog/contact.html')
