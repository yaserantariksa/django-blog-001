from django import forms
from django.core import paginator
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from .models import Category, Post
from .forms import NewCommentForm, PostSearchForm
from django.views.generic import ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.core import serializers
from django.http import JsonResponse

# Create your views here.

def postslist(request):
    posts = Post.newmanager.all()
    page = request.GET.get('page',1)
    paginator = Paginator(posts, 5)

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request,'blog/index.html',{'posts':posts})


def detailpost(request,post):
    post = get_object_or_404(Post, slug=post, status='published')

    allcomments = post.comments.filter(status=True)
    page = request.GET.get('page',1)
    paginator = Paginator(allcomments,5)

    try:
        comments = paginator.page(page)
    except PageNotAnInteger:
        comments = paginator.page(1)
    except EmptyPage:
        comments = paginator.page(paginator.num_pages)

    user_comment = None
    comment_form = NewCommentForm()

    if request.method == "POST":
        comment_form = NewCommentForm(request.POST)
        if comment_form.is_valid():
            user_comment = comment_form.save(commit=False)
            user_comment.post = post
            user_comment.save()
            return HttpResponseRedirect("/" + post.slug)
        else:
            comment_form = NewCommentForm()

    return render(
        request,
        "blog/detailpost.html",
        {
            "post":post,
            "comments":user_comment,
            "comments" : comments,
            "comment_form" : comment_form,
            "allcomments" : allcomments,
        },
    )

class CatListView(ListView):
    template_name = 'blog/category.html'
    context_object_name = 'catlist'

    def get_queryset(self):
        content = {
            'cat' : self.kwargs['category'],
            'posts' : Post.objects.filter(category__name=self.kwargs['category']).filter(status='published')
        }

        return content

def category_list(request):
    category_list = Category.objects.exclude(name='default')

    context = {
        'category_list': category_list
    }
    return context

def post_search(request):
    form = PostSearchForm()
    q = ''
    c = ''
    results = []
    query = Q()

    if request.POST.get('action') == 'post':
        search_string = str(request.POST.get('ss'))
        if search_string is not None:
            search_string = Post.objects.filter(title__contains=search_string)[:3]

            data = serializers.serialize('json',list(search_string), fields=('id','tittle','slug','title'))

            return JsonResponse({'search_string':data})

    if 'q' in request.GET:
        form = PostSearchForm(request.GET)
        if form.is_valid():
            q = form.cleaned_data['q']
            c = form.cleaned_data['c']

            if c is not None:
                query &= Q(category=c)
            if q is not None:
                query  &= Q(title__contains=q)

            results = Post.objects.filter(query)
            
    return render(request, 'blog/search.html',{'form':form,'q':q, 'results':results})