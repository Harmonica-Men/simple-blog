from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views import View
from .models import Post, Category
from .forms import PostForm
from django.urls import reverse_lazy


#class based view
class FrontpageView(ListView):
    model = Post
    template_name = 'frontpage.html'
    ordering = ['-post_date']

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(FrontpageView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


def CategoryListView(request):
    cat_menu_list = Category.objects.all()
    return render(request, 'category_list.html', {'cat_menu_list':cat_menu_list})


class CategoryView(View):
    template_name = 'categories.html'
    error_template_name = '404.html'

    def get(self, request, cats):
        try:
            category = get_object_or_404(Category, name=cats)
            category_posts = Post.objects.filter(category=category)
            context = {
                'cats': category.name,
                'category_posts': category_posts,
            }
            return render(request, self.template_name, context)
        except Http404:
            return render(request, self.error_template_name, status=404)

class BlogPostDetailView(DetailView):
    model = Post
    template_name = 'blogpost.html'

    # def get_context_data(self, *args, **kwargs):
    #    cat_menu = Category.objects.all()
    #    context = super(BlogPostDetailView, self).get_context_data(*args, **kwargs)
    #    context["cat_menu"] = cat_menu
    #    return context


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


class AddCategoryView(CreateView):
    model = Category
    template_name = 'add_category.html'
    fields = '__all__'
    #fields = ('title', 'title_tag', 'body'  )


