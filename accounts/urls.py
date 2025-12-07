from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView
from django.urls import reverse_lazy
from . import views

app_name = 'accounts'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', 
         auth_views.LogoutView.as_view(
             template_name='registration/logged_out.html',
             next_page=reverse_lazy('core:home')
         ), 
         name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('profile/', views.profile, name='profile'),
]

