from django.urls import path
from .views import FrontpageView, BlogPostDetailView, AddPostView, UpdatePostView, DeletePostView, AddCategoryView, CategoryView
from .views import CategoryView


urlpatterns = [
    
    path('', FrontpageView.as_view(), name= 'frontpage'),
    path('article/<int:pk>', BlogPostDetailView.as_view(), name= 'article-detail'),
    path('add_post/', AddPostView.as_view(), name= 'add_post'),    
    path('add_category/', AddCategoryView.as_view(), name= 'add-category'),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name= 'update-post'),
    path('article/<int:pk>/remove', DeletePostView.as_view(), name= 'delete-post'),
    path('category/<str:cats>/', CategoryView.as_view(), name='category'),
]

