from django.urls import path
from .views import postslist, detailpost

app_name = 'blog'
urlpatterns = [
    path('',postslist,name='postlist'),
    path('<slug:post>/',detailpost, name='detailpost'),
]