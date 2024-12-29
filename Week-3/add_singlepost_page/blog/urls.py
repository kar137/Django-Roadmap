from django.urls import path
from . import views

urlpatterns = [
    path('', views.starting_page, name="starting-page"),
    path('posts', views.posts, name="posts-page"),
    path('posts/<slug>', views.post_detail, name="post-detail-page"),   #posts/my_first_post  --> often said to be slug
]