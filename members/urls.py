from django.urls import path, include
from .views import UserRegisterView, UserEditView, CustomPasswordChangeView
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import PasswordChangeView



urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('edit_profile/', UserEditView.as_view(), name='edit-profile'),
    # path('<int:pk>/password/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('<int:pk>/password/', CustomPasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'), name='password_change_done'),
    # path('<int:uid>/', include('members.urls')),
    # 4edit_profile, name='edit-profile'),
    # path('article/edit/<int:pk>', UpdatePostView.as_view(), name= 'update-post'),
    # path('article/<int:pk>/remove', DeletePostView.as_view(), name= 'delete-post'),
    # path('<int:uid>/', include('members.urls')),
]
