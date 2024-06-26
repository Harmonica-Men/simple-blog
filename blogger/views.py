from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post
from .forms import PostForm

class FrontpageView(ListView):
    model = Post
    template_name = 'frontpage.html'


class BlogPostDetailView(DetailView):
    model = Post
    template_name = 'blogpost.html'


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    #fields = '__all__'
    #fields = ('title', 'title_tag', 'body'  )


