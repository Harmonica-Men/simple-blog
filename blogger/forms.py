from django import forms
from .models import Post, Category, Comment

# choices = [('coding', 'coding'), ('sports', 'sports'), ('voetbal', 'voetbal')]
choices = Category.objects.all().values_list('name', 'name')

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # fields = ['title', 'title_tag']
        fields = ('title', 'title_tag', 'author', 'category', 'body', 'image')

        widgets = {
            'title' : forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'placeholder test'}),
            
            'title_tag' : forms.TextInput(attrs={'class': 'form-control'}),
            'author' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'user name', 'id': 'js_id', 'type': 'hidden'}),
            #  : forms.Select(attrs={'class': 'form-control'}),
            'category' : forms.Select(choices=choices, attrs={'class': 'form-control'}),
            'body' : forms.Textarea(attrs={'class': 'form-control'}),            
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')
        # fields = ('title', 'title_tag', 'author', 'category', 'body', 'image')

        widgets = {
            'name' : forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'placeholder test'}),
            'body' : forms.Textarea(attrs={'class': 'form-control'}),
        }