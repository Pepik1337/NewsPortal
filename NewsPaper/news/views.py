from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from .models import Post


class PostList(ListView):
    model = Post
    ordering = 'created_datetime'
    template_name = 'Posts.html'
    context_object_name = 'posts'


class PostDetail(DetailView):
    model = Post
    template_name = 'Post.html'
    context_object_name = 'post'