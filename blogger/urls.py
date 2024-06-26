from django.urls import path
#from . import views
from .views import FrontpageView, BlogPostDetailView, AddPostView


urlpatterns = [
    #path('', views.frontpage, name = "frontpage"),
    path('', FrontpageView.as_view(), name= 'frontpage'),
    path('article/<int:pk>', BlogPostDetailView.as_view(), name= 'article-detail'),
    path('add_post/', AddPostView.as_view(), name= 'add_post'),
]
