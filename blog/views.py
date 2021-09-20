from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.

def postslist(request):
    posts = Post.newmanager.all()

    return render(request,'blog/index.html',{'posts':posts})


def detailpost(request,post):
    post = get_object_or_404(Post, slug=post, status='published')

    return render(request,'blog/detailpost.html',{'post':post})