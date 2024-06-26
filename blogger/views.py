from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

class FrontpageView(ListView):
    model = Post

    template_name = 'frontpage.html'


class BlogPostDetailView(DetailView):
    model = Post
    template_name = 'blogpost.html'

# Create your views here.
# def frontpage(request):
# return render(request, 'frontpage.html', {})
