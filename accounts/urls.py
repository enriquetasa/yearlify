from django.urls import path

from django.contrib.auth import views as auth_views
from accounts import views

app_name = 'account'

urlpatterns = [
    path(r'_login/', auth_views.LoginView.as_view(), name='login'),
    path(r'_register/', views.register, name='register'),
    path(r'_logout/', auth_views.LogoutView.as_view(), name='logout'),
]
