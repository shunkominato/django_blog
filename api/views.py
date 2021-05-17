from django.shortcuts import render
from django.views.generic import ListView

from .models import Blog

class BlogListView(ListView):
    template_name = 'blog/blog_list.html'
    model = Blog
