from django.urls import path
from .views import CatListView, post_search, postslist, detailpost

app_name = 'blog'
urlpatterns = [
    path('',postslist,name='postlist'),
    path('<slug:post>/',detailpost, name='detailpost'),
    path("category/<category>/",CatListView.as_view(),name='category'),
    path("search/search",post_search,name='searchpost'),
]