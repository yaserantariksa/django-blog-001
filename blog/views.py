from django.shortcuts import render
from .models import Post
from django.views.generic import ListView

# Create your views here.

class PostListView(ListView):
    model = Post
    # paginate_by = 3
    template_name = 'blog/index.html'
    ordering = ['-published_date']

