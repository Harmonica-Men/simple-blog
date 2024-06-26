from django.urls import path
#from . import views
from .views import FrontpageView, BlogPostDetailView, AddPostView, UpdatePostView


urlpatterns = [
    #path('', views.frontpage, name = "frontpage"),
    path('', FrontpageView.as_view(), name= 'frontpage'),
    path('article/<int:pk>', BlogPostDetailView.as_view(), name= 'article-detail'),
    path('add_post/', AddPostView.as_view(), name= 'add_post'),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name= 'update-post'),
]
