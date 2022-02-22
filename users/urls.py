from django.urls import path 
from django.contrib.auth.views import LogoutView
from .views import register, change_password, login, UpdateUserView,ProfileView, UpdateProfileView
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView, PasswordChangeView, PasswordChangeDoneView
 
 
 
urlpatterns = [
    path('register/', register, name='register'),
    
    path('change_password/', change_password, name='change_password'),
    
    path('login/', login, name='login'),
    
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    
    path('update_user/<int:pk>/', UpdateUserView.as_view(), name='update_user'),
    
    
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    
    path('update_profile/<int:pk>/', UpdateProfileView.as_view(), name='update_profile'),
    
    

     
]

