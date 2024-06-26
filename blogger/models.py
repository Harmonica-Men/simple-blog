from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date


class Category(models.Model):
     name = models.CharField(max_length=200)
#     # title = models.CharField(max_length=255)
#     # slug = models.SlugField(unique=True)


     class Meta:
#         ordering = ('name',)
         verbose_name_plural = 'Categories'

     def __str__(self):
         return self.name

     def get_absolute_url(self):
         return reverse('frontpage') 

class Post(models.Model):
    ACTIVE = 'active'
    DRAFT = 'draft'

    CHOICES_STATUS = (
    (ACTIVE, 'Active'),
    (DRAFT, 'Draft')
    )

    #category = models.ForeignKey(Category, related_name='posts', on_delete=models.CASCADE)
    
    title = models.CharField(max_length=200)
    title_tag = models.CharField(max_length=200)
    author = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    slug = models.SlugField()
    intro = models.TextField()
    body = models.TextField()
    post_date = models.DateField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=CHOICES_STATUS, default=ACTIVE)
    category = models.CharField(max_length=200, default='codeing')

    
    
    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # return reverse('article-detail', args=(str(self.id)))
        return reverse('frontpage') 
        # return f'/{self.category.slug}/{self.slug}/'
