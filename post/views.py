from django.shortcuts import render
from .models import Post
from django.views.generic import ListView

# Create your views here.
class PostListView(ListView):
    model = Post
    template_name = 'post/post_list.html'
    context_object_name = 'post_list'
    ordering = ['-date_create']