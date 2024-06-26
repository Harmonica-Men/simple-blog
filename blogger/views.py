from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm
from django.urls import reverse_lazy

class FrontpageView(ListView):
    model = Post
    template_name = 'frontpage.html'
    ordering = ['-id']


class BlogPostDetailView(DetailView):
    model = Post
    template_name = 'blogpost.html'


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    #fields = '__all__'
    #fields = ('title', 'title_tag', 'body'  )

class UpdatePostView(UpdateView):
    model = Post   
    template_name = 'update_post.html'
    fields = ('title', 'title_tag', 'body')


class DeletePostView(DeleteView):
    model = Post   
    template_name = 'delete_post.html'
    success_url = reverse_lazy('frontpage')


