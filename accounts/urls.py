from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Login and logout views provided by Django's authentication system
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Registration view (custom implementation in views.py)
    path('register/', views.register, name='register'),
]
