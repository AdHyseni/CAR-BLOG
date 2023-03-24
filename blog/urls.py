from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('blogs/',views.blogs,name='blogs'),
    path('blog/<slug:slug>/', views.BlogDetails.as_view(),name='blog'),
    path('contact/',views.contact,name='contact'),
]